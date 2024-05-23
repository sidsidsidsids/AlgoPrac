// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0]);
const M = Number(input[1]);
const place = input[2].split(" ").map(Number);
const ld = place[0];
const rd = N - place[M-1];
let min = Math.max(ld, rd);
let max = N;
let answer = N;
while (min <= max) {
  mid = Math.floor((min+max)/2);
  let flag = true;
  for (let i = 1; i < M; i++) {
    if (Math.ceil((place[i] - place[i-1]) / 2) > mid) {
      flag = false;
      break;
    }
  }
  if (flag) {
    answer = Math.min(answer, mid);
    max = mid - 1
  } else {
    min = mid + 1
  }
}

console.log(answer)