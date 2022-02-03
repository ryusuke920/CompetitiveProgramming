#include<stdio.h>
int main(void){
int ch1[110]={0},ch2[110]={0},a,b,c,d, ans=0;
scanf("%d%d%d%d", &a,&b,&c,&d);
ans = ((b-a)+(d-c)-abs(a-c)-abs(b-d)) / 2;
if(ans<0) ans=0;
printf("%d\n",ans);
return 0;
}