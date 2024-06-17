const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

let i = 0
while (true) {
    let f1 = input[i].split(" ").map(Number)
    if (!f1[0]) break;
    let f2 = input[i+1].split(" ").map(Number)
    
    const Lf1 = f1[0]
    let F1 = Array(20001).fill(0)
    for (let j = 1; j <= Lf1; j++) {
        const num = f1[j]
        F1[num + 10000] = 1
    }
    
    const Lf2 = f2[0]
    let F2 = Array(20001).fill(0)
    for (let j = 1; j <= Lf2; j++) {
        const num = f2[j]
        F2[num + 10000] = 1
    }    
    let v1 = 0;
    let v2 = 0;
    let answer = 0
    for (let k = 0; k < 20001; k++) {
        if (F1[k] && F2[k]) {
            answer += (k - 10000) + Math.max(v1, v2)
            v1 = 0
            v2 = 0
        } else if (F1[k]) {
            v1 += k - 10000
        } else if (F2[k]) {
            v2 += k - 10000
        }
    }
    answer += Math.max(v1, v2)
    console.log(answer)
    i += 2
}