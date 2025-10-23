# Python Template

A minimal, well-structured Python project template with modern tooling and best practices built in. Perfect for quickly starting new Python projects with proper dependency management, code formatting, and environment configuration.

## Features

- Modern Python packaging with `pyproject.toml`
- Pydantic for configuration and data validation
- Environment variable management with python-dotenv
- Ruff for fast linting and code formatting
- Proper package structure with `src/` layout
- Ready-to-use virtual environment setup

## What's Included

This template demonstrates:
- Loading configuration from environment variables (.env file)
- Type-safe configuration using Pydantic models
- Proper package structure that can be installed with pip
- Pre-configured Ruff linting rules for code quality
- Module execution (`python -m src`)

## Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

1. Clone or download this template:
```bash
git clone <your-repo-url>
cd python-template-master
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate it (Linux/Mac)
source .venv/bin/activate

# Or on Windows
.venv\Scripts\activate
```

3. Install the package in editable mode:
```bash
pip install -e .
```

4. (Optional) Create a `.env` file for your environment variables:
```bash
echo "API_KEY=your_api_key_here" > .env
```

### Running the Application

Run as a Python module:
```bash
python -m src
```

Or execute directly:
```bash
python src/main.py
```

### Expected Output
```
API Key: your_api_key_here
```
(Or "no .env file found with API_KEY" if no .env file is present)

## Project Structure

```
.
├── src/
│   ├── __init__.py      # Package initialization
│   ├── __main__.py      # Entry point for module execution
│   └── main.py          # Main application logic
├── pyproject.toml       # Project metadata and dependencies
└── README.md           # This file
```

## Customization

### Adding Dependencies

Edit `pyproject.toml` and add your dependencies to the `dependencies` array:
```toml
dependencies = [
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
    "your-package-here>=1.0.0",
]
```

Then reinstall:
```bash
pip install -e .
```

### Code Formatting and Linting

This template uses Ruff for both linting and formatting. Ruff is pre-configured in `pyproject.toml`.

Check for issues:
```bash
ruff check src/
```

Auto-fix issues:
```bash
ruff check --fix src/
```

Format code:
```bash
ruff format src/
```

### Environment Variables

Add any environment variables your application needs to a `.env` file in the project root. They will be automatically loaded by `python-dotenv` when the application starts.

## Next Steps

1. Rename the project in `pyproject.toml` (name, description, authors)
2. Add your application logic to `src/main.py`
3. Create additional modules in the `src/` directory as needed
4. Update dependencies in `pyproject.toml`
5. Customize the Ruff configuration if needed
6. Update this README with your project-specific information

## Dependencies

- **pydantic** (>=2.0.0) - Data validation and settings management using Python type annotations
- **python-dotenv** (>=1.0.0) - Load environment variables from .env files

## License

MIT