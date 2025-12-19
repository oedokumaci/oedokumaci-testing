"""Oedokumaci Testing package.

Testing this great template
"""

from __future__ import annotations

from loguru import logger

from oedokumaci_testing._internal.cli import get_parser, main
from oedokumaci_testing._internal.logging import configure_logging

__all__: list[str] = ["configure_logging", "get_parser", "logger", "main"]
