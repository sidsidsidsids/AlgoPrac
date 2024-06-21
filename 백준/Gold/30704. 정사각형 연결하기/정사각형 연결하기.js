const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const T = Number(input[0])
let answer = []
for (let i = 0; i < T; i++) {
    const N = Number(input[i + 1])
    const j = Math.floor(Math.sqrt(N))
    const sq = j * j
    if (N > sq) {
        const k = j * (j + 1)
        if (N <= k) {
            answer.push((j + (j + 1)) * 2)
        } else {
            answer.push(((j + 1) + (j + 1)) * 2)
        }
    } else {
        answer.push((j + j) * 2)
    }
}
console.log(answer.join("\n"))