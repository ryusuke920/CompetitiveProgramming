/*ABC221-A */
function Main(input) {
    input = input.split("\n");
    tmp = input[0].split(" ");
    A = parseInt(tmp[0]);
    B = parseInt(tmp[1]);
    console.log(32 ** (A - B));
  }
  Main(require("fs").readFileSync("/dev/stdin", "utf8"));  