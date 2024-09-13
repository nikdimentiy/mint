# Consonant Substring Value Calculator

This Python script calculates the highest value of consonant substrings from a list of strings. The value of each consonant substring is determined by summing the positions of the letters in the alphabet (where 'a' = 1, 'b' = 2, ..., 'z' = 26). Additionally, the script creates a beautiful bar chart to visually display the highest values of consonant substrings for each test case. 🎉📊

## Key Features

- **Consonant Value Calculation**: The script replaces vowels with spaces to highlight consonant substrings and then computes their total value.
- **Result Visualization**: Using the `matplotlib` library, a bar chart is created to show the highest values of consonant substrings for each input string.
- **User-Friendly Output**: Results are displayed in a neat table using the `PrettyTable` library, making them easy to read. 📋✨

## How to Run the Script

To run this script and see the results, follow these simple steps:

1. **Install Required Libraries**:
   Make sure you have Python installed. You will also need to install the `matplotlib` and `prettytable` libraries if you haven't done so already. Just run the following command in your terminal:

   ```bash
   pip install matplotlib prettytable
   ```

2. **Save the Script**:
   Copy the code into a text editor and save it as `consonant_substring_value_calculator.py`.

3. **Run the Script**:
   Open your terminal or command prompt, navigate to the folder where you saved the script, and execute the command:

   ```bash
   python consonant_substring_value_calculator.py
   ```

4. **View the Results**:
   After running the script, a table will appear in your terminal showing the input strings and their highest consonant substring values. A bar chart will also be created and saved as `result_plot.jpg` in the same folder. Open this file to see a visual representation of the results. 📈🌟

## Example Output

When you run the script, you will see something like this in your terminal:

```
+---------------------+-------------------------------------+
|        Input        | Highest Consonant Substring Value   |
+---------------------+-------------------------------------+
|      strength       |                 98                  |
|       rhythm        |                 72                  |
|     algorithm       |                 67                  |
|         a           |                  0                  |
|        bcdf         |                 10                  |
|       python        |                 77                  |
|      example        |                 36                  |
|       hello         |                 22                  |
|       world         |                 72                  |
|     testcase        |                 66                  |
|    beautiful        |                 0                   |
|        sky          |                 55                  |
|        xyz          |                 75                  |
+---------------------+-------------------------------------+
```

And the bar chart saved as `result_plot.jpg` will visually showcase the highest values of consonant substrings for each test case. Enjoy your analysis! 🎨📈

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify any sections to better fit your project's needs!
