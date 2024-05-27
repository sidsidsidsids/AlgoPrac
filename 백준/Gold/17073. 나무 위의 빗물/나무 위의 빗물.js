// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const NM = input[0].split(' ').map(Number);
const N = NM[0];
const M = NM[1];
let graph = Array.from({length : N + 1}, () => [])
for (let i = 0; i < N-1; i++) {
    const [U, V] = input[i+1].split(' ').map(Number);
    graph[U].push(V);
    graph[V].push(U);
}
let visit = Array(N + 1).fill(false);
let stk = [1];
let leaf = [];
visit[1] = true;
while (stk.length > 0) {
    let node = stk.pop();
    let isLeaf = true;
    graph[node].forEach(elem => {
        if (visit[elem] == false) {
            stk.push(elem);
            visit[elem] = true;
            isLeaf = false;
        }
    })
    if (isLeaf == true) {
        leaf.push(node);
    }
}
console.log(M / leaf.length)