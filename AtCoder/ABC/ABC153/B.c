#include<stdio.h>
int main(void){
int H, N, A[100010], sum=0;
scanf("%d%d", &H , &N);
for(int i=0;i<N;i++){
    scanf("%d", &A[i]);
    sum+=A[i];
}
if(sum>=H){
printf("Yes\n");
}else{
printf("No\n");
}
}