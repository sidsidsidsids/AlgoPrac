// const input = require('fs').readFileSync('./input.txt', 'utf8').split("\n")
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

let N = parseInt(input[0])
let classinfo = input[1].split(" ").map((e) => Number(e))
let [B, C] = input[2].split(" ").map((e) => Number(e))

const func = (N, classinfo, B, C) => {
    let answer = 0
    for (let i = 0;i < N;i++) {
        classinfo[i] -= B
        answer += 1
        if (classinfo[i] > 0) {
            if (classinfo[i] % C == 0) {
                answer += Math.floor(classinfo[i] / C)
            } else {
                answer += Math.floor(classinfo[i] / C) + 1
            }
        }
    }
    return answer
}

console.log(func(N, classinfo, B, C))
