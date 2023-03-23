// CodeWars task -> solution: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/javascript

function drawStairs(n) {
  let stairs = "";
  for (let i = 0; i < n; i++) {
    stairs += " ".repeat(i) + "I\n";
  }
  return stairs.slice(0, -1);
}
