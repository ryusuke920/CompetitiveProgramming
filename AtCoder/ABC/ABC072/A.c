#include<stdio.h>
int main(void){
int X, t, ans=0;
scanf("%d%d", &X,&t);
ans = X-t;
if(ans<0) ans=0;
printf("%d\n",ans);
return 0;
}