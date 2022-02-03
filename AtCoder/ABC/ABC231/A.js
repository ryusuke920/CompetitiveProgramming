function Main(input) {
    D = parseInt(input);
    console.log(D / 100);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));