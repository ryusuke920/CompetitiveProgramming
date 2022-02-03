#include<stdio.h>
int main(void){
int H, A,sum=0;
scanf("%d%d", &H , &A);
while(H>0){
    H-=A;
    sum+=1;
}
printf("%d\n", sum);
return 0;
}