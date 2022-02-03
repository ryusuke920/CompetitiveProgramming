#include<stdio.h>
int main(void){
int N=0, ch=0;
long long int A[100010]={0};
scanf("%d", &N);
for(int i=0;i<N;i++){
    scanf("%d", &A[i]);
}
for(int i=0;i<N-1;i++){
    for(int j=1; j<N && i<j ;j++){
        if(A[i]==A[j]){
            ch+=1;
        }
    }
}
if(ch==0){
    printf("Yes\n");
}else{
    printf("No\n");
}
return 0;
}