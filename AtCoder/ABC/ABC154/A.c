#include<stdio.h>
#include<string.h>
int main(void){
char S[20], T[20], U[20];
int A=0, B=0, n=0, sum=0;
scanf("%s%s", S, T);
scanf("%d%d", &A, &B);
scanf("%s", U);
n=strlen(U);
for(int i=0;i<n;i++){
if(U[i]==S[i]){
    sum+=1;
}
}
if(sum==n){
printf("%d %d\n",A-1, B);
}else{
printf("%d %d\n",A, B-1);  
}
return 0;
}