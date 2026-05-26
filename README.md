# MainG2L

A Python utility library providing common helper functions for strings, math, and files — a practical reference for general coding patterns.

## Project structure

```
MainG2L/
├── main.py            # Demo entry point
├── utils/
│   ├── __init__.py    # Re-exports all public helpers
│   ├── string_utils.py
│   ├── math_utils.py
│   └── file_utils.py
└── tests/
    ├── test_string_utils.py
    ├── test_math_utils.py
    └── test_file_utils.py
```

## Utilities

### String (`utils/string_utils.py`)

| Function | Description |
|---|---|
| `capitalize_words(text)` | Title-case every word in a string |
| `truncate(text, max_length, suffix="...")` | Shorten a string to a maximum length |
| `is_palindrome(text)` | Return `True` when the string reads the same forwards and backwards (ignores case and spaces) |
| `count_words(text)` | Count whitespace-separated words |
| `reverse_string(text)` | Reverse the characters in a string |

### Math (`utils/math_utils.py`)

| Function | Description |
|---|---|
| `factorial(n)` | Compute n! for a non-negative integer |
| `is_prime(n)` | Return `True` when n is prime |
| `fibonacci(n)` | Return the first n Fibonacci numbers as a list |
| `clamp(value, minimum, maximum)` | Clamp a value to [minimum, maximum] |
| `percentage(part, total)` | Compute what percentage part is of total |

### File (`utils/file_utils.py`)

| Function | Description |
|---|---|
| `read_lines(filepath)` | Read all lines from a text file |
| `write_lines(filepath, lines)` | Write a list of lines to a text file |
| `file_exists(filepath)` | Return `True` when a regular file exists at the path |
| `count_lines(filepath)` | Count the number of lines in a file |

## Running the demo

```bash
python main.py
```

## Running the tests

```bash
python -m pytest tests/ -v
```
