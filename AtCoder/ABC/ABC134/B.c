#include<stdio.h>
int main(void){
int N, D;
scanf("%d%d",&N, &D);
if(N%(D*2+1)==0) printf("%d\n",N/(D*2+1));
else printf("%d\n",N/(D*2+1)+1);
return 0;
}