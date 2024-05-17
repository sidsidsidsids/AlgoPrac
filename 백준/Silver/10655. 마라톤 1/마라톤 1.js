// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0]);
let array = new Array(N)
for (let n = 0; n < N; n++) {
  const location = input[n+1].split(" ")
  const num_loc = location.map(Number)
  array[n] = num_loc
}

let value = 0
for (let i = 1; i < N; i++) {
  value += Math.abs(array[i][0] - array[i-1][0]) + Math.abs(array[i][1] - array[i-1][1]);
}

let result = value
for (let i = 1; i < N-1; i++) {
  let temp = value
  temp -= Math.abs(array[i][0] - array[i-1][0]) + Math.abs(array[i][1] - array[i-1][1]);
  temp -= Math.abs(array[i][0] - array[i+1][0]) + Math.abs(array[i][1] - array[i+1][1]);
  temp += Math.abs(array[i-1][0] - array[i+1][0]) + Math.abs(array[i-1][1] - array[i+1][1]);
  if (temp < result) {
    result = temp
  }
}

console.log(result)