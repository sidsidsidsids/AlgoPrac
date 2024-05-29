// const input = require("fs").readFileSync("./input.txt", "utf8").split("\n");
const input = require('fs').readFileSync('/dev/stdin').toString().split("\n")

let [numA, numB] = input[0].split(' ').map(BigInt);
if (numA < numB) {
    [numA, numB] = [numB, numA];
}
while (numB > 0n) {
    [numA, numB] = [numB, numA % numB];
}
console.log("1".repeat(Number(numA)))