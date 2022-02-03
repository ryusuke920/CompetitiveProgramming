#include<stdio.h>
int main(void){
char S[4], T[4];
int n=0;
scanf("%s%s", S, T);
for(int i=0; i<3; i++){
    if(S[i]==T[i]){
n+=1;
    }
}
printf("%d", n);
return 0;
}