const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0])
let answer = []
for (let i = 0; i < N; i++) {
    const [x, y] = input[i + 1].split(" ").map(Number)
    const dist = y - x
    const square = Math.floor(Math.sqrt(dist))
    let cnt = square * 2 - 1
    const rest = dist - square * square
    if (rest > 0) {
        rest <= square ? cnt += 1 : cnt += 2
    }
    answer.push(cnt)
}
console.log(answer.join("\n"))