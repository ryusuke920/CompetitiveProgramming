#include<stdio.h>
int main(void){
char S[10];
scanf("%s",S);
if(S[0]=='S'){
    printf("Cloudy");
}else if(S[0]=='C'){
    printf("Rainy"); 
}else {
    printf("Sunny"); 
}
return 0;
}