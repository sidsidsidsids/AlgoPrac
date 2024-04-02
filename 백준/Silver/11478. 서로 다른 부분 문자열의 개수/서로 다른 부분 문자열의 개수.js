const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const S = input[0]

const func = (S) => {
    let answer = 0
    const N = S.length
    let set = new Set()
    for (let i = 0; i < N; i++) {
        partial_string = ''
        for (let j = i; j < N; j ++) {
            partial_string += S[j]
            if (!set.has(partial_string)) {
                set.add(partial_string)
                answer += 1   
            }
        }
    }
    return answer
}

console.log(func(S))
