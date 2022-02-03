#include<stdio.h>
int main(void){
int X,Y,Z, ch=0,ans=0;
scanf("%d%d%d", &X, &Y, &Z);
ch=Y+Z*2;
for(int i=ch;i<=X;i+=(Y+Z)){
    ans++;
}
printf("%d\n",ans);
return 0;
}