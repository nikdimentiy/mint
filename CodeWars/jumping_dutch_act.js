// # CodeWars task -> solution: https://www.codewars.com/kata/570bcd9715944a2c8e000009/javascript

function sc(floor) {
  if (floor <= 1) return "";

  return "Aa~ ".repeat(floor - 1) + "Pa!" + (floor <= 6 ? " Aa!" : "");
}
