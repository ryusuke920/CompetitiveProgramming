function main(input) {
    inputs = input.split(' ');
    const n = parseInt(inputs[0]);
    const k = parseInt(inputs[1]);
    const a = parseInt(inputs[2]);

    let ans = (a + k - 1) % n;

    if (ans === 0) {
        console.log(n);
    } else{
        console.log(ans);
    }
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));