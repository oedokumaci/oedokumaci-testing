"""Command-line interface for oedokumaci_testing."""

from __future__ import annotations

from loguru import logger

from oedokumaci_testing._internal.logging import configure_logging


def main() -> None:
    """Main entry point for the CLI."""
    # json_logs=False for human-readable output during development
    # Set to True for production (structured JSON logs)
    configure_logging(level="INFO", json_logs=False)
    logger.info("Starting Oedokumaci Testing...")

    # Your application logic here

    logger.info("Run finished.")


__all__ = ["main"]
