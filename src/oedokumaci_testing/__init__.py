"""Oedokumaci Testing package.

Testing this great template
"""

from __future__ import annotations

from oedokumaci_testing._internal.cli import main
from oedokumaci_testing._internal.logging import configure_logging
from oedokumaci_testing._internal.path import DATA_DIR, PACKAGE_DIR

__version__ = "0.0.0"
__all__: list[str] = ["DATA_DIR", "PACKAGE_DIR", "configure_logging", "main"]
