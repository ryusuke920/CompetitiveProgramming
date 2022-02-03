#include<stdio.h>
int main(void){
char S[5];
scanf("%s", S);
if((S[0]==S[1] && S[1]==S[2] && S[2]==S[0]) || (S[0]!=S[1] && S[1]!=S[2] && S[2]!=S[0])){
    printf("No\n");
}else{
    printf("Yes\n");
return 0;
}
}