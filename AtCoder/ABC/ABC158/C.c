#include<stdio.h>
int main(void){
int A, B, M=0, N=0;
int i=0, j=0;
scanf("%d%d", &A, &B);
while(i*0.08<=A){
    i=i+1;
    M=i;
}
while(j*0.10<=B){
    j=j+1;
    N=j;
}
if(M>N){
    for(int i=N;i<M;i++){
        i*0.10<=B;
        N=i;
    }
    printf("%d\n",M);
}else if(M<N){
    for(int j=M;i<N;j++){
        j*0.08<=A;
        M=i;
    }
    printf("%d\n",N);
}else{
    printf("-1\n");
}
return 0;
}