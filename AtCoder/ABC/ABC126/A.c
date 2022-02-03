#include<stdio.h>
int main(void){
int N, K;
char S[100];
scanf("%d%d", &N, &K);
scanf("%s" ,S);
S[K-1]+=32;
printf("%s" ,S);
return 0;
}