#include<stdio.h>
int main(void){
long int N, A, B, num, p;
scanf("%ld%ld%ld", &N, &A, &B);
    num=N/(A+B);
    p=N%(A+B);
if(N%(A+B)==0){
    printf("%ld\n",num*A);
}else if(N%(A+B)!=0 && p<=A){
    printf("%ld\n",num*A+p);
}else{
    printf("%ld\n",num*A+A);
}
return 0;
}