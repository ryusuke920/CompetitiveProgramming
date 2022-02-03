#include<stdio.h>
int main(void){
int N, R;
scanf("%d%d",&N, &R);
if(N>10)printf("%d\n", R);
else printf("%d\n",R+(10-N)*100);
return 0;
}