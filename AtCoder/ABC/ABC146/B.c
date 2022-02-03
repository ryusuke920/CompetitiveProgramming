#include<stdio.h>
#include<string.h>
int main(void){
int N,T;
char S[10001];
scanf("%d%s", &N, S);
for(int i=0; i<strlen(S); i++){
T=S[i]-'A';
T = (T+N) % 26;
S[i]='A'+T;
}
printf("%s\n", S);
return 0;
}