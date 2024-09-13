# Consonant Substring Value Calculator

This Python project provides a function to calculate the highest value of consonant substrings in a given string. Each consonant's value is determined by its position in the English alphabet (a=1, b=2, ..., z=26). The project includes a set of test cases to demonstrate the functionality of the code.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Test Cases](#test-cases)
- [Example Output](#example-output)
- [License](#license)

## Features

- Calculates the highest value of consonant substrings in a string.
- Ignores vowels and focuses solely on consonants.
- Displays results in a formatted table for easy readability.

## Installation

To run this code, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, you will need the `PrettyTable` library for displaying results in a table format. You can install it using pip:

```bash
pip install prettytable
```

## Usage

1. Clone the repository or download the code file.
2. Run the script in your Python environment.

```bash
python consonant_substring_value.py
```

## Functionality

The main function in this code is `solve(s: str) -> int`, which takes a string `s` as input and returns the highest value among all consonant substrings. The function works as follows:

1. It defines a set of vowels to identify consonants.
2. It calculates the value of each character based on its position in the alphabet.
3. It extracts consonant substrings by replacing vowels with spaces and splitting the string.
4. It computes the total value for each consonant substring and returns the maximum value found.

## Test Cases

The code includes several test cases to demonstrate its functionality:

```python
test_cases = [
    "zodiacs",
    "strength",
    "cozy",
    "xyzzy",
    "zodiac",
    "chruschtschov",
    "khrushchev",
    "twelfthstreet",
    "mischtschenkoana"
]
```

## Example Output

When you run the script, it will display the results in a formatted table:

```
+---------------------+-------------------------------------+
|        Input        | Highest Consonant Substring Value   |
+---------------------+-------------------------------------+
|       zodiacs       |                 26                  |
|      strength       |                 92                  |
|        cozy         |                 34                  |
|       xyzzy         |                 75                  |
|       zodiac        |                 26                  |
|  chruschtschov      |                104                  |
|     khrushchev      |                 96                  |
|   twelfthstreet     |                108                  |
|  mischtschenkoana   |                145                  |
+---------------------+-------------------------------------+
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.
