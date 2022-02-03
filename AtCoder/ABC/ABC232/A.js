function Main(input) {
    s = input;
    x = parseInt(s[0]);
    y = parseInt(s[2]);

    console.log(x * y);

}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));