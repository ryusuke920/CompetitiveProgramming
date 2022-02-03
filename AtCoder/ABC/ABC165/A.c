#include<stdio.h>
int main(void){
    int K, A, B, count=0;
    scanf("%d%d%d",&K,&A,&B);
    for(int i=A;i<=B;i++){
        if(i%K==0){
            count++;
        }
    }
    if(count!=0)printf("OK\n");
    else printf("NG\n");
return 0;
}