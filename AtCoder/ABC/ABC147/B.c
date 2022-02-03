#include<stdio.h>
#include<string.h>
int main(void){
char S[101];
int n, sum=0;
scanf("%s", S);
n=strlen(S);
for(int i=0;i<n;i++){
 if( S[i]!=S[n-(i+1)] ){
  sum+=1;
 }
}
printf("%d", sum/2);
return 0;
}