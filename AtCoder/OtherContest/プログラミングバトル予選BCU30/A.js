function main (input) {
	var n = input.split('\n');
	var a = n[1].split(" ");

	for (var i = 0; i <= 29; i++) {
		var count = 0;
		for (var j = 0; j < a.length; j++) {
			if (a[j] == i) {
				count++
			}
		}
		process.stdout.write(count + " ");
	}
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));