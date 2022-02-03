#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int main(void){
char S[200];
bool a=true;  
scanf("%s", S);
for(int i=0;i<strlen(S);i++){
    if((i%2==0) && (S[i]!='R' && S[i]!='U' && S[i]!='D') ){
        a=false;
    }else if((i%2==1) && (S[i]!='L' && S[i]!='U' && S[i]!='D') ){
        a=false;
    }
}
if(a==true){
    printf("Yes\n");
}else{
    printf("No\n");
}
return 0;
}