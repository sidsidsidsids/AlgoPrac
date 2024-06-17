const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const F = Array(318138).fill(1)
F[0] = 0
F[1] = 0
let M = [0]
let cnt = 1
for(let i = 2; i < 318138; i++) {
    if (F[i]) {
        for (let j = i + i; j < 318138; j += i) {
            F[j] = 0
        }
        if (F[cnt++]) {
            M.push(i)
        }
    }
}
const T = Number(input[0])
for (let t = 0; t < T; t++) {
    const n = Number(input[t+1])
    console.log(M[n])
}