// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const [A, B, L] = input[0].split(' ').map(Number);
function gcd(a, b) {
    if (a < b) {
        [a, b] = [b, a]
    }
    while (b > 0) {
        [a, b] = [b, a % b]
    }
    return a
}
const lcm = Math.floor((A * B) / gcd(A, B))
let d = []
for (let i = 0; i < Math.floor(L ** 0.5) + 1; i++) {
    if (L % i == 0) {
        d.push(i)
        d.push(L / i)
    }
}
d.sort((a, b) => a-b)
let flag = false
for (const e of d) {
    if (Math.floor(lcm * e / gcd(lcm, e)) == L) {
        console.log(e)
        flag = true
        break
    }
}
if (!flag) {
    console.log(-1)
}