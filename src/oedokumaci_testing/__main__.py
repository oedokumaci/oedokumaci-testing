"""Entry point for running the package as a module.

This allows running the package via:
    uv run python -m oedokumaci_testing
"""

from oedokumaci_testing._internal.cli import main

if __name__ == "__main__":
    main()
