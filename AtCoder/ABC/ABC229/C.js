function main(input) {
    inputs = input.split('\n');
    const n = parseInt(inputs[0].split(' ')[0]);
    let w = BigInt(inputs[0].split(' ')[1]);

    const ab = [];
    for (let i = 0; i < n; i ++) {
        const a = BigInt(inputs[i + 1].split(' ')[0]);
        const b = BigInt(inputs[i + 1].split(' ')[1]);

        ab.push([a, b]);

    }

    ab.sort((a, b) => Number(b[0] - a[0]));

    let ans = 0n;
    for (let i = 0; i < n; i ++) {
        if (w - ab[i][1] >= 0) {
            ans += ab[i][0] * ab[i][1];
            w -= ab[i][1];
        } else {
            ans += ab[i][0] * w;
            break; 
        }
    }

    console.log(ans.toString());

}

main(require('fs').readFileSync('/dev/stdin', 'utf8')); 