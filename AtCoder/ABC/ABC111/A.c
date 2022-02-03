#include<stdio.h>
#include<string.h>
int main(void){
char n[4];
scanf("%s", n); 
for(int i=0;i<strlen(n);i++){
    if(n[i]=='1'){
        n[i]='9';
    }else{
        n[i]='1';
    }
}
printf("%s\n", n); 
return 0;
}