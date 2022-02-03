#include<stdio.h>
int main(void){
int N, K , H[200010], sum=0, sumn=0;
scanf("%d%d", &N , &K);
for(int i=0;i<N;i++){
    scanf("%d", &H[i]);
}
for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
        if(H[i]<H[j]){
            sumn=H[i];
            H[i]=H[j];
            H[j]=sumn;
        }
    }
}//整順
for(int i=0;i<N;i++){
    printf("%d ", H[i]);
}
}