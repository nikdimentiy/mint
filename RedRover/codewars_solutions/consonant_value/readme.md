

## Consonant Substring Value Calculator

This Python script calculates the highest value of consonant substrings in a given string. It's a useful tool for analyzing string patterns and character values in various applications, such as linguistics or cryptography.

### Features

- Calculates the value of consonant substrings in a string
- Handles multiple test cases efficiently
- Presents results in a clear, tabular format using PrettyTable

### How it works

1. The `solve` function takes a string input and returns the highest value among all consonant substrings.
2. Consonants are assigned values based on their position in the alphabet (a=1, b=2, ..., z=26).
3. The function splits the input string into consonant substrings by treating vowels as separators.
4. It then calculates the value of each consonant substring and returns the maximum value.

### Usage

```python
from prettytable import PrettyTable
from consonant_value_calculator import solve

# Example usage
result = solve("zodiacs")
print(result)  # Output: 26
```

### Test Cases

The script includes several test cases to demonstrate its functionality:

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

### Output

The script uses PrettyTable to display results in a formatted table:

```
+------------------+-----------------------------------+
|      Input       | Highest Consonant Substring Value |
+------------------+-----------------------------------+
|     zodiacs      |                 26                |
|     strength     |                 57                |
|       cozy       |                 22                |
|      xyzzy       |                 72                |
|      zodiac      |                 26                |
|  chruschtschov   |                104                |
|    khrushchev    |                 80                |
|  twelfthstreet   |                 73                |
| mischtschenkoana |                 80                |
+------------------+-----------------------------------+
```

### Requirements

- Python 3.x
- PrettyTable library (`pip install prettytable`)

### Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/consonant-substring-value/issues) if you want to contribute.

### License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.
