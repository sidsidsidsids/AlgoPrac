// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0]);
let dist = input[1].split(" ").map(Number)
let price = input[2].split(" ").map(Number)
let result = BigInt(0);
let p_i = 0;
while (p_i < N-1) {
  let k = 1;
  while (p_i + k < N && BigInt(price[p_i]) <= BigInt(price[p_i + k])) {
    k++
  }
  for (let i = p_i; i < p_i + k; i++) {
    if (i == N-1) {
      break
    }
    result += BigInt(price[p_i]) * BigInt(dist[i]);      
  }
  if (p_i + k >= N) {
    break
  }
  p_i += k
}
console.log(result.toString())