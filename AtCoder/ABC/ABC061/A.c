#include<stdio.h>
int main(void){
int A,B,C;
scanf("%d%d%d",&A,&B,&C);
if(C>=A && C<=B) printf("Yes\n");
else printf("No\n");
return 0;
}