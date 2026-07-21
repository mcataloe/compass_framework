"""Command-line entry point for validation and atomic release."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .constants import EXIT_INVALID, VALIDATOR_VERSION
from .contracts import ContractError, load_inputs
from .engine import ResumeReleaseEngine
from .name_integrity import verify_name_integrity


class ReleaseArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        self.exit(EXIT_INVALID, f"{self.prog}: error: {message}\n")


def build_parser() -> argparse.ArgumentParser:
    parser = ReleaseArgumentParser(
        prog="python -m tools.resume_release",
        description="Validate and atomically release COMPASS resume artifacts.",
    )
    parser.add_argument("--version", action="version", version=VALIDATOR_VERSION)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "release"):
        command = subcommands.add_parser(
            name,
            help=(
                "validate staged artifacts without publishing"
                if name == "validate"
                else "validate and publish only after aggregate PASS"
            ),
        )
        command.add_argument("--docx", type=Path, help="staged DOCX artifact")
        command.add_argument("--markdown", type=Path, help="staged Markdown artifact")
        command.add_argument("--contract", type=Path, required=True, help="release contract JSON")
        command.add_argument("--coverage", type=Path, help="employment coverage plan JSON")
        command.add_argument(
            "--visual-attestation", type=Path, help="every-page visual-review attestation JSON"
        )
        command.add_argument(
            "--manifest-out", type=Path, required=True, help="staging manifest output path"
        )
        command.add_argument(
            "--render-dir", type=Path, required=True, help="staging directory for rendered pages"
        )
        if name == "release":
            command.add_argument("--output-docx", type=Path, help="final DOCX path")
            command.add_argument("--output-markdown", type=Path, help="final Markdown path")
    verify_name = subcommands.add_parser(
        "verify-name-integrity",
        help="verify actual artifact names after publication or attachment",
    )
    verify_name.add_argument("--contract", type=Path, required=True, help="release contract JSON")
    verify_name.add_argument(
        "--receipt", type=Path, required=True, help="artifact-name integrity receipt JSON"
    )
    verify_name.add_argument(
        "--report-out", type=Path, required=True, help="name-integrity report output path"
    )
    return parser


def _invocation_error(message: str) -> int:
    print(f"resume-release: {message}", file=sys.stderr)
    return EXIT_INVALID


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "verify-name-integrity":
        try:
            return verify_name_integrity(args.contract, args.receipt, args.report_out)
        except ContractError as exc:
            return _invocation_error(str(exc))
        except OSError as exc:
            print(
                f"resume-release: name verification could not complete ({exc.__class__.__name__})",
                file=sys.stderr,
            )
            return 2
    if args.docx is None and args.markdown is None:
        return _invocation_error("at least one staged artifact is required")
    if args.command == "release":
        if args.output_docx is None and args.output_markdown is None:
            return _invocation_error("release requires at least one final output path")
        if args.output_docx is not None and args.docx is None:
            return _invocation_error("--output-docx requires --docx")
        if args.output_markdown is not None and args.markdown is None:
            return _invocation_error("--output-markdown requires --markdown")
    final_paths = [
        path
        for path in (
            getattr(args, "output_docx", None),
            getattr(args, "output_markdown", None),
        )
        if path is not None
    ]
    if any(args.manifest_out.resolve() == path.resolve() for path in final_paths):
        return _invocation_error("the staging manifest path cannot be a final artifact path")
    try:
        loaded = load_inputs(args.contract, args.coverage, args.visual_attestation)
        args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
        args.render_dir.mkdir(parents=True, exist_ok=True)
        _, exit_code = ResumeReleaseEngine().run(
            mode=args.command,
            loaded=loaded,
            docx_path=args.docx,
            markdown_path=args.markdown,
            manifest_out=args.manifest_out,
            render_dir=args.render_dir,
            output_docx=getattr(args, "output_docx", None),
            output_markdown=getattr(args, "output_markdown", None),
        )
        return exit_code
    except ContractError as exc:
        return _invocation_error(str(exc))
    except OSError as exc:
        print(
            f"resume-release: validation could not complete ({exc.__class__.__name__})",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
