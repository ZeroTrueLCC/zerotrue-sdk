# Contributing to ZeroTrue Python SDK

Thank you for your interest in contributing to ZeroTrue Python SDK!

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/sdk-python.git
   cd sdk-python
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Style

- Follow PEP 8 style guide
- Use `black` for code formatting (line length: 140)
- Use `ruff` for linting
- Use type hints for all functions

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=zerotrue --cov-report=html

# Run specific test file
pytest tests/test_client.py
```

## Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Run tests and linting:
   ```bash
   # Pre-commit will run automatically on commit, or run manually:
   pre-commit run --all-files

   # Or run individually:
   ruff check .
   ruff format .
   pytest
   ```

4. Commit your changes:
   ```bash
   git commit -m "feat: your feature description"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request

## Commit Message Format

We use conventional commits format:

- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code refactoring
- `docs:` - Documentation changes
- `test:` - Test changes
- `chore:` - Other changes

Example: `feat: added support for custom timeout`

## Questions?

Feel free to open an issue or contact support@zerotrue.ai

