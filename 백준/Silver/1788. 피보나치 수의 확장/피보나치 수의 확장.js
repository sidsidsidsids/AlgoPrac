const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

let N = Number(input[0])
let fibo = Array(1000001).fill(0)
fibo[1] = 1
for (let i = 2; i < 1000001; i++) {
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 1000000000
}
let buho = 0
if (N > 0) {
    buho = 1
} else if (N < 0) {
    if (N % 2 == 0) {
        buho = -1
    } else {
        buho = 1
    }
}

console.log(buho)
console.log(N >= 0 ? fibo[N] : fibo[-N])