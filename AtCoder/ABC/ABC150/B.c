#include<stdio.h>
int main(void){
int N, ch=0;
char S[100];
scanf("%d%s", &N, S);
for(int i=0; i<=N; i++){
    if(S[i]=='A' && S[i+1]=='B' &&S[i+2]=='C'){
  ch+=1;
  }
}
 printf("%d",ch);
return 0;
}