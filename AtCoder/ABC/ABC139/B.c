#include<stdio.h>
int main(void){
int A, B, sum=0, ch=0;
scanf("%d%d", &A , &B);
sum+=A;
if(A>B && B==1){
    printf("0\n");
}else{
while(1){
    if(sum>=B){
        break;
    }
    sum+=A-1;
    ch++;
}
printf("%d\n", ch+1); 
}
return 0;
}