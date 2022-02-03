#include<stdio.h>
#include<string.h>
int main(void){
char S[110];
int n=0;
scanf("%s", S);
n=strlen(S);
for(int i=0;i<n;i++){
S[i]='x';
printf("%c",S[i]);
}
return 0;
}