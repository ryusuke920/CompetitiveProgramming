#include<stdio.h>
int main(void){
int A,B;
scanf("%d%d",&A,&B);
if(A%3==0 || B%3==0 || (A+B)%3==0) printf("Possible\n");
else printf("Impossible");
return 0;
}