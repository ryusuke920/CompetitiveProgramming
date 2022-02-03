#include<stdio.h>
int main(void){
int A, B, C, sum=0;
scanf("%d%d%d", &A, &B, &C);
sum=10*A+B+C;
if(10*B+A+C>sum){
    sum=10*B+A+C;
}else if(10*C+A+B>=sum){
    sum=10*C+A+B;
}
printf("%d\n",sum);
return 0;
}