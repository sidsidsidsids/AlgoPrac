// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0])
let grid= [];
for (let i = 1; i < N+1; i++) {
    grid.push(input[i].split(" ").map(e => e.replace('\r','')));
}
let teachers = [];
for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (grid[i][j] == "T") {
            teachers.push([i, j]);
        }
    }
}
let flag = false;
function place(i, j, cnt) {
    if (flag) 
        return
    if (cnt == 3) {
        const result = check();
        if (result) {
            flag = true;
        }
        return
    }
    if (grid[i][j] == 'X') {
        grid[i][j] = 'O'
        if (j+1 < N && i < N) {
            place(i, j+1, cnt + 1)
        }
        else if (j < N && i+1 < N) {
            place(i+1, 0, cnt + 1)
        }
        grid[i][j] = 'X'
        if (j+1 < N && i < N) {
            place(i, j+1, cnt)
        }
        else if (j < N && i+1 < N) {
            place(i+1, 0, cnt)
        }
    }
    else {
        if (j+1 < N && i < N) {
            place(i, j+1, cnt)
        }
        else if (j < N && i+1 < N) {
            place(i+1, 0, cnt)
        }
    }
}

function check() {
    let able = true
    teachers.forEach((e) => {
        const i = e[0]
        const j = e[1]
        for (let ni = i+1; ni < N; ni++) {
            const t = grid[ni][j]
            if (t == 'S') {
                able = false
                break;
            } else if (t == 'O') break;
        }
        for (let ni = i-1; ni > -1; ni--) {
            const t = grid[ni][j]
            if (t == 'S') {
                able = false
                break;
            } else if (t == 'O') break;
        }
        for (let nj = j+1; nj < N; nj++) {
            const t = grid[i][nj]
            if (t == 'S') {
                able = false
                break;
            } else if (t == 'O') break;
        }
        for (let nj = j-1; nj > -1; nj--) {
            const t = grid[i][nj]
            if (t == 'S') {
                able = false
                break;
            } else if (t == 'O') break;
        }
    })
    return able
}
place(0,0,0)
console.log(flag ? "YES" : "NO")