#include<stdio.h>
int main(void){
int R;
scanf("%d",&R);
if(R<1200)printf("ABC\n");
else if(1200<=R && R<2800)printf("ARC\n");
else printf("AGC\n");
return 0;
}