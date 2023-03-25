// CodeWars task solution: https://www.codewars.com/kata/62c93765cef6f10030dfa92b/javascript

function solution(start, finish) {
  const dp = new Array(finish + 1).fill(Infinity);
  dp[start] = 0;
  for (let i = start + 1; i <= finish; i++) {
    dp[i] = Math.min(dp[i - 1], i >= 3 ? dp[i - 3] : Infinity) + 1;
  }
  return dp[finish];
}
