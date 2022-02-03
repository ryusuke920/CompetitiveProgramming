function main(input) {
    inputs = input.split(' ');
    s = parseInt(inputs[0]);
    t = parseInt(inputs[1]);
    x = parseInt(inputs[2]);

    if (s < t) {
        if (s <= x && x < t) {
            console.log('Yes');
        } else {
            console.log('No');
        }
    } else {
        tmp = s;
        s = t;
        t = tmp;
        if (s <= x && x < t) {
            console.log('No');
        } else {
            console.log('Yes');
        }
    }

}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));