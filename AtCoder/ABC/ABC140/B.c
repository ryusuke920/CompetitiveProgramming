#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int main(void){
int N, A[100], B[100], C[100], sum=0;
scanf("%d", &N);
for(int i=0;i<N;i++){
    scanf("%d", &A[i]);
}
for(int i=0;i<N;i++){
    scanf("%d", &B[i]);
    sum+=B[i];
}
for(int i=0;i<N-1;i++){
    scanf("%d", &C[i]);
}
for(int i=1;i<N;i++){
    if(A[i]-A[i-1]==1){
        sum+=C[A[i-1]-1];
    }
}
printf("%d", sum);
return 0;
}