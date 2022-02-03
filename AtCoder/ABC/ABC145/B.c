#include<stdio.h>
#include<string.h>
int main(void){
int N, a, ch=0;
char S[110];
scanf("%d%s", &N, S);
a=strlen(S)/2;
for(int i=0; i<a; i++){
    if(S[i]==S[a+i]){
    ch+=1;  
    }
}
if(ch == a && ch!=0 && strlen(S) %2 == 0){
printf("Yes\n");
}else{
printf("No\n");
}
return 0;
}