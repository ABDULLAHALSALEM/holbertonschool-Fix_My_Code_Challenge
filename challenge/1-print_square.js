#!/usr/bin/node

function printSquare(size) {
    for (let i = 0; i < size; i++) {
        let line = "";
        for (let j = 0; j < size; j++) {
            line += "#";
        }
        console.log(line);
    }
}

if (process.argv.length <= 2) {
    console.log("Usage: ./1-print_square.js <size>");
    process.exit(1);
}

const size = parseInt(process.argv[2], 10);
printSquare(size);
