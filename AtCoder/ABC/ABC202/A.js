function main(input){
    const args = input.split(' ');
    const a = parseInt(args[0], 10);
    const b = parseInt(args[1], 20);
    if ((a * b) % 2 == 0){
        console.log("Even");
    }else{
        console.log("Odd");
    }
}

main(require("fs").readFileSync("/dev/stdin", "utf8"));