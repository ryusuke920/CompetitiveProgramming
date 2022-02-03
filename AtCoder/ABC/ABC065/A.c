#include<stdio.h>
int main(void){
int X,A,B;
scanf("%d%d%d",&X,&A,&B);
if(A-B>=0)printf("delicious\n");
else if(B-A<=X) printf("safe\n");
else printf("dangerous\n");
return 0;
}