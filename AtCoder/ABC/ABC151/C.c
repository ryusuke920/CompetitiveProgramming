#include<stdio.h>
int main(void){
int N, M;
int ac[100001]={0}, wa[100001]={0},good=0, bad=0;
scanf("%d%d", &N, &M);
int P[M];
char S[M][3];
for(int i=0;i<M;i++){
    scanf("%d%s", &P[i], S[i]);
if(S[i][0]=='A' && ac[P[i]]==0){
     ac[P[i]]=1;
  }else if(S[i][0]=='W' &&ac[P[i]]==0){
      wa[P[i]]+=1;
  }
}
for(int i=0;i<=N;i++){
    if(ac[i]){
    good+=ac[i];
    bad+=wa[i];
    }
}
printf("%d %d\n", good, bad);
return 0;
}