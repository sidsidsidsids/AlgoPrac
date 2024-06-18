const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0])
const nArr = input[1].split(" ").map(Number)
let Ns = new Set()
nArr.forEach(e => {
    Ns.add(e)
})
const M = Number(input[2])
const mArr = input[3].split(" ").map(Number)
for (let i = 0; i < M; i++) {
    console.log(Ns.has(mArr[i]) ? 1 : 0)
}