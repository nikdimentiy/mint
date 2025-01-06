/**
 * Generates a string representing a staircase of height `n`.
 * Each step of the staircase is represented by the character 'I',
 * with each subsequent step indented by an increasing number of spaces.
 *
 * @param {number} n - The number of steps in the staircase.
 * @returns {string} - A string representation of the staircase.
 */
function drawStairs(n) {
  let stairs = ""; // Initialize an empty string to store the staircase
  for (let i = 0; i < n; i++) {
    // Append a step with 'I' followed by a newline, preceded by 'i' spaces
    stairs += " ".repeat(i) + "I\n";
  }
  // Remove the last newline character before returning the string
  return stairs.slice(0, -1);
}

// Driver code to test the function
console.log(drawStairs(3));
// Output:
// I
//  I
//   I

console.log(drawStairs(5));
// Output:
// I
//  I
//   I
//    I
//     I
