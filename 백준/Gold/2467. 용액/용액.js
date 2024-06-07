const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
let l = 0;
let r = N-1;
let al;
let ar;
let av = 2000000001;
let v;
while (l < r) {
    let ll = arr[l]
    let rr = arr[r]
    v = ll + rr;
    dv = Math.abs(v);
    if (dv < av) {
        av = dv
        al = ll
        ar = rr
    }
    if (v == 0) break;
    else if (v < 0) l++;
    else if (v > 0) r--;
}
console.log(al, ar);