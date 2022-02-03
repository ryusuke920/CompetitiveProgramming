#include<stdio.h>
#include<string.h>
#include <stdlib.h>
int main(void){
int N,a[100010]={},ch=0//フラグ;
scanf("%d", &N);
char S[200010][11];
for(int i=0;i<N;i++){
    scanf("%s", S[i]);
}
//昇順に並べる
qsort(S,N,11,strcmp);
for(int i=0; i<N-1;i++){
    if(!strcmp(S[i],S[i+1])){
        a[i+1] += a[i];
    }
}
for(int i=0;i<N;i++){
    if(a[i]==ch){
        printf("%s\n", s[i]);
    }
}
return 0;
}