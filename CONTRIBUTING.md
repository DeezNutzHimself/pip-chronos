# Contributing to pipup

Thank you for your interest in contributing to pipup! This document provides guidelines and instructions for contributing.

## Development Setup

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/deeznutz6942o/pipup.git
   cd pipup
   ```

2. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes and add tests if applicable.

3. Run tests:
   ```bash
   pytest
   ```

4. Format your code:
   ```bash
   black .
   isort .
   ```

5. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```

6. Push your branch to your fork:
   ```bash
   git push origin feature-name
   ```

7. Create a pull request to the main repository.

## Code Style

We follow the [Black](https://black.readthedocs.io/en/stable/) code style. The pre-commit hooks will automatically format your code.

## Releasing

For maintainers, to create a new release:

1. Update version in `pipup/__init__.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Commit the changes
4. Create a new tag with the version number
5. Push the tag to GitHub
6. Build and upload to PyPI:
   ```bash
   python -m build
   twine upload dist/*
   ```

## License

By contributing to pipup, you agree that your contributions will be licensed under the project's MIT license. 