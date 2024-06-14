const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0]);
let arr = []
for (let i = 0; i < N; i++) {
    arr.push(Number(input[i+1]))
}
arr.sort((a, b) => a-b)
let answer = 0
for (let i = 0; i < N; i++) {
    answer += Math.abs(i+1 - arr[i])
}
console.log(answer)