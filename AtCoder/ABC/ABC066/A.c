#include<stdio.h>
int main(void){
int a,b,c;
scanf("%d%d%d",&a,&b,&c);
if((a+b)<=(a+c)&&(a+b)<=(b+c)) printf("%d\n",a+b);
else if((a+c)<=(a+b)&&(a+c)<=(b+c)) printf("%d\n",a+c);
else printf("%d\n",b+c);
return 0;
}