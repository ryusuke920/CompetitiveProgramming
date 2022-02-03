#include<stdio.h>
int main(void){
int N, K, ch=0;
scanf("%d%d", &N, &K);
while(N!=0){
    ch+=1;
    N=N/K;
}
printf("%d\n", ch);
return 0;
}