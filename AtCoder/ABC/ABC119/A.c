#include<stdio.h>
int main(void){
char S[15];
scanf("%s", S);
if(S[5]=='0' && S[6]<='4' &&S[6] >='1'){
printf("Heisei\n");
}else{
printf("TBD\n");  
}
return 0;
}