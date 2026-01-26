"""Tests for the main module entry point."""

from __future__ import annotations

import subprocess
import sys


def test_main_runs_successfully() -> None:
    """Test that the main module can be executed."""
    result = subprocess.run(
        [sys.executable, "-m", "oedokumaci_testing"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0


def test_main_function_import() -> None:
    """Test that main function can be imported."""
    from oedokumaci_testing import main

    assert callable(main)
