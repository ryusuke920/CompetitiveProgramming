#include<stdio.h>
int main(void){
char S[5];
scanf("%s", &S);

if((S[0]==S[1]&&S[2]==S[3] &&S[0]!=S[2])||
      (S[0]==S[2]&&S[1]==S[3] && S[0]!=S[1])|| 
         (S[0]==S[3]&&S[1]==S[2] &&S[0]!=S[1])){
    printf("Yes\n");
}else {
    printf("No\n");
}
return 0;
}