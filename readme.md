# Random Password Generator

A simple Python package that generates secure random passwords. The generator supports both standard random generation using `random.choice()` and cryptographically secure generation using `os.urandom()`.

## Features

- Generate passwords of customizable length
- Option to use cryptographically secure random generation
- Input validation for minimum password length
- Includes special characters, numbers, and letters
- Unit tests included

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Parth-243/Python-Project-random-password-generator-.git
cd password-generator
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

### As a Script

Run directly from the command line:

```bash
python src/password_generator.py
```

### As a Module

```python
from src.password_generator import PasswordGenerator

# Create a generator instance
generator = PasswordGenerator()

# Generate a password with default length (12 characters)
password = generator.generate_password()

# Generate a password with custom length
password = generator.generate_password(length=16)

# Generate a password using os.urandom()
secure_password = generator.generate_password(use_os_random=True)
```

## Running Tests

```bash
python -m unittest discover tests
```
