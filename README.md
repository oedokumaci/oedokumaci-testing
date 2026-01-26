# Oedokumaci Testing

[![ci](https://github.com/oedokumaci/oedokumaci-testing/workflows/ci/badge.svg)](https://github.com/oedokumaci/oedokumaci-testing/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://oedokumaci.github.io/oedokumaci-testing/)

Testing this great template

## Installation

```bash
uv add git+https://github.com/oedokumaci/oedokumaci-testing
```

Or with pip:

```bash
pip install git+https://github.com/oedokumaci/oedokumaci-testing
```


## Logging

- Uses [loguru](https://github.com/Delgan/loguru) with JSON output to stderr by default (no log file is written unless you ask for one).
- Programmatic control: `from oedokumaci_testing._internal.logging import configure_logging` to customize level, JSON/human format, and optional `log_file`.

## Developer Workflow

### Setup

```bash
git clone https://github.com/oedokumaci/oedokumaci-testing
cd oedokumaci-testing
make setup
```

### Development Cycle

1. **Create a feature branch**

    ```bash
    git switch -c feat/my-feature
    # or for bug fixes:
    git switch -c fix/bug-description
    ```

2. **Make changes and commit** (follow [Angular commit convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit))

    ```bash
    git add .
    git commit -m "feat: Add new feature"
    ```

3. **Clean up commits with [interactive rebase](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_changing_multiple)** (optional but recommended)

    ```bash
    git rebase -i main
    ```

4. **Run quality checks**

    ```bash
    make format  # Auto-format code
    make check   # Run all quality checks (lint, types, docs, API)
    make test    # Run test suite
    ```

5. **Open a Pull Request** — prefer **rebase merge** to keep a clean history

### Release (maintainers only, on `main` branch)

After merging PRs:

```bash
git switch main
git pull

make changelog   # Update CHANGELOG.md with new entries
make coverage    # Generate coverage report

# Check the changelog for the new version (x.y.z), then:
make release version=x.y.z

# Verify the updated documentation locally:
make docs
```
