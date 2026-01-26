"""Oedokumaci Testing package.

Testing this great template
"""

from __future__ import annotations

from oedokumaci_testing._internal.cli import main
from oedokumaci_testing._internal.logging import configure_logging

__version__ = "0.0.0"
__all__: list[str] = ["configure_logging", "main"]
