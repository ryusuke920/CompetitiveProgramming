function Main(input) {
    inputs = input.trim().split('\n');
    l = parseInt(inputs[0].split(' ')[0]);
    r = parseInt(inputs[0].split(' ')[1]);
    s = inputs[1];

    const x = s.slice(0, l - 1);
    const y = s.slice(l - 1, r).split('').reverse().join('')
    const z = s.slice(r);

    const ans = x + y + z;
    console.log(ans);

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));