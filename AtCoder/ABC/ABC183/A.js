function main(input){
    const args = input.split(" ");
    const a = parseInt(args[0]);
    let ans;
    if (a >= 0){
        ans = a;
    } else{
        ans = 0;
    }

    console.log(ans);
}

main(require('fs').readFileSync('/dev/stdin', 'utf8')); // 入力するために必要？