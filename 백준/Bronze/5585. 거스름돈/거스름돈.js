// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

const money = Number(input[0]);
let rest = 1000 - money;
let count = 0
const coins = [500, 100, 50, 10, 5, 1]
coins.forEach(coin => {
  if (rest >= coin) {
    const value = Math.floor(rest / coin)
    count += value
    rest -= value * coin
  }
});
console.log(count)