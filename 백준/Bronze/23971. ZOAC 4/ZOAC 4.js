let input = require('fs').readFileSync('/dev/stdin').toString().split(" ")
// input = [5, 4, 1, 1]
let H = parseInt(input[0])
let W = parseInt(input[1])
let N = parseInt(input[2])
let M = parseInt(input[3])
let garo = 0
let sero = 0
let i = 0
while (i < H) {
    garo += 1
    i += 1 + N
}
i = 0
while (i < W) {
    sero += 1
    i += 1 + M
}
console.log(garo * sero)