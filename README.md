# Python Template

## Setup and Run

### Prerequisites
- Python 3.8 or higher

### Installation

1. Clone or download this repository

2. Create virtual environment:
```bash
python -m venv .venv
```

3. Activate virtual environment:
```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -e .
```

### Run the Script

Run as module:
```bash
python -m src
```

Or run directly:
```bash
python src/main.py
```

### Expected Output
```
User info: John Doe is 30 years old and lives in New York, NY 10001
Total users: 2
Math result: 15.0
```

## What This Does

- Creates and validates user data using Pydantic models
- Demonstrates data validation (email, phone, zip code)
- Performs basic math operations
- Manages user collections

## Dependencies

- pydantic[email] - Data validation and settings management