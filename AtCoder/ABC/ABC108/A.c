#include<stdio.h>
int main(void){
int K,ch=0;
scanf("%d", &K);
for(int i=1;i<=K;i+=2){
    for(int j=2;j<=K;j+=2){
        ch+=1;
    }
}
printf("%d\n",ch);
return 0;
}