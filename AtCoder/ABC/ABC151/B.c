#include<stdio.h>
#include<string.h>
int main(void){
int N, K, M, A[200], sum=0, x;
scanf("%d%d%d", &N, &K, &M);
for(int i=0; i<N-1; i++){
    scanf("%d", &A[i]);
    sum+=A[i];
}
if( sum >= N*M ){
    printf("0\n");
}else if( (N*M)-sum > K ){
    printf("-1\n");
}else{
    printf("%d\n", (N*M)-sum);
}
return 0;
}