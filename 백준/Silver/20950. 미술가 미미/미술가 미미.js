const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0])
const paints = Array(N)
for (let n = 0; n < N; n++) {
    const elem = input[n+1].split(" ").map(Number)
    paints[n] = elem
}
const gomduri = input[N+1].split(" ").map(Number)

const M = Math.min(N, 7)
function combination(arr, limit) {
    let result = []

    function combine(cur, start, maxima) {
        if (cur.length === maxima) {
            result.push(cur.slice())
            return
        }

        for (let i = start; i < N; i++) {
            cur.push(arr[i])
            combine(cur, i+1, maxima)
            cur.pop()
        }
    }
    for (let i = 2; i <= limit; i++) {
        combine([], 0, i)
    }

    return result
}
let idxArray = []
for (let i = 0; i < N; i++) {
    idxArray.push(i)
}

const cases = combination(idxArray, M)
let diff = 255 * 3 + 1
const [gomRed, gomGrn, gomBlu] = gomduri
cases.forEach(e => {
    const elemLen = e.length
    let red = 0
    let grn = 0
    let blu = 0
    e.forEach(idx => {
        red += paints[idx][0]
        grn += paints[idx][1]
        blu += paints[idx][2]
    })
    red = Math.floor(red / elemLen)
    grn = Math.floor(grn / elemLen)
    blu = Math.floor(blu / elemLen)
    diff = Math.min(diff, Math.abs(gomRed - red) + Math.abs(gomGrn - grn) + Math.abs(gomBlu - blu))
})

console.log(diff)