function main(input) {
    n = parseInt(input);
    if (n >= 42) {
        n += 1
    }
    console.log('AGC' + ('00' + n).slice(-3));

}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));