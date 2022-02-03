function Main(input) {
    inputs = input.split(' ');
    const x = parseInt(inputs[0]);
    const y = parseInt(inputs[1]);

    if (x >= y) {
        console.log(0);
    } else {
        console.log(Math.ceil((y - x) / 10));
    }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));