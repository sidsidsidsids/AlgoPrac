// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const T = Number(input[0]);
for (let t = 1; t < T + 1; t++) {
  const info = input[t].split(" ");
  const x1 = Number(info[0]);
  const y1 = Number(info[1]);
  let r1 = Number(info[2]);
  const x2 = Number(info[3]);
  const y2 = Number(info[4]);
  let r2 = Number(info[5]);

  const dx = x1 - x2;
  const dy = y1 - y2;
  if (r1 > r2) {
    const temp = r1;
    r1 = r2;
    r2 = temp;
  }
  const rSum = (r1 + r2) * (r1 + r2);
  const rSub = (r2 - r1) * (r2 - r1);
  const d = dx * dx + dy * dy;

  if (d < rSum && d > rSub) {
    console.log(2);
  } else if (d === rSum || (d === rSub && d !== 0)) {
    console.log(1);
  } else if (d < rSub || d > rSum) {
    console.log(0);
  } else if (d === 0) {
    if (r1 === r2) {
      console.log(-1);
    } else {
      console.log(0);
    }
  }
}
