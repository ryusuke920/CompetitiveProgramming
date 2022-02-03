function main(input) {
    inputs = input.split('\n');
    s1 = inputs[0];
    s2 = inputs[1];

    if ((s1 === '#.' && s2 === '.#') || (s1 === '.#' && s2 === '#.')) {
        console.log('No');
    } else {
        console.log('Yes');
    }
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));