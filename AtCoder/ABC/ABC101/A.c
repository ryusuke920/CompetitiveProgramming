#include<stdio.h>
int main(void){
char S[5];
int A=0, B=0;
scanf("%s",&S);
for(int i=0;i<4;i++){
    if(S[i]=='+') A++;
    else B++;
}
printf("%d\n",A-B);
return 0;
}