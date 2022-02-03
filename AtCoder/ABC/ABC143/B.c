#include<stdio.h>
int main(void){
int N, d[100], sum=0;
scanf("%d", &N);
for(int i=0;i<N;i++){
scanf("%d", &d[i]);
};
for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
        if(i!=j){
    sum+=d[i]*d[j];
        }
    }
}
printf("%d", sum/2);
return 0;
}