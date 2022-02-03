#include<stdio.h>
int main(void){
int r,g,b,ans;
scanf("%d%d%d",&r,&g,&b);
ans=r*100+g*10+b;
if(ans%4==0) printf("YES\n");
else printf("NO\n");
return 0;
}