# 🔐 Secure Password Generator (Python)

A customizable, secure password generator built in Python. Supports multiple configuration options including character types, easy-to-read formatting, and more.

---

## 📁 Project Structure
<pre>
├── main.py # Core password generator function + validators
├── user_input.py # CLI tool to generate passwords via user input 
├── wrapper.py # Script wrapper for static password generation
├── utils.py # Helper functions
└── README.md # This README file </pre>

## 🚀 How to Use

### Option 1: Run via CLI (interactive)
Run the following in your terminal:
```bash
python user_input.py
```

You’ll be prompted to enter:

- Password length (8–16)
- Whether to enable easy-to-read mode
- If yes, you’ll pick a mode (1–5)
- Whether to include:

    - Uppercase letters
    - Digits
    - Special characters

### Option 2: Call Programmatically (Example is wrapper.py)
```bash

from main import password_generator

# Example
print(password_generator(length=12, easy_to_read=True, esr_mode=2, use_upper=True, use_digits=True, use_special=False))
```

## Parameters

| Parameter      | Type           | Default | Description                                                                                      |
|----------------|----------------|---------|--------------------------------------------------------------------------------------------------|
| `length`       | `int` or `str` | `16`    | Desired password length (must be between 8 and 16)                                               |
| `use_upper`    | `bool`         | `True`  | Include uppercase letters                                                                        |
| `use_digits`   | `bool`         | `True`  | Include digits (0–9)                                                                             |
| `use_special`  | `bool`         | `True`  | Include special characters (`!@#$%^&*()`)                                                        |
| `easy_to_read` | `bool`         | `False` | Restrict digits/specials to start or end of password                                             |
| `esr_mode`     | `int` or `str` | `5`     | Layout modes for `easy_to_read` (see below)                                                      |

### `esr_mode` Options

- `1`: special + main + digits  
- `2`: digits + main + special  
- `3`: (special + digits) + main  
- `4`: main + (special + digits)  
- `5`: Randomly start or end

## Features
- Minimum 1 character from each enabled category
- No repeated characters in a password (when possible)
- Input validation (boolean and integer checks)
- Customizable layout in "easy-to-read" mode
- Default fallback values for all parameters
- Self-adjusting logic to meet formatting and uniqueness constraints

## Example Output
Generated password: !DytmwOj75918320

## Tech Used
- Python 3.6+

    This project uses only built-in modules:

    - random
    - string
    - re

© Author
Created by KB Garcia.