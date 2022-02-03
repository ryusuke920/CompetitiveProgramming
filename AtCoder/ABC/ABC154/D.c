#include<stdio.h>
int main(void){
int N, K, num=0;
double sum=0.0,sum2=0.0;
scanf("%d%d",&N, &K);
int p[200010]={0};
for(int i=0;i<N;i++){
    scanf("%d", &p[i]);
}
for(int i=0;i<K-3;i++){
    if(sum<p[i]+p[i+1]+p[i+2]){
sum=p[i]+p[i+1]+p[i+2];
num=i;//最大の時の場所
}
printf("%d\n\n\n",num);
for(int t=0;t<K;t++){
    for(int j=0;p[num+j]<p[num+j];j++){
        sum2+=(p[j]/p[num+t]);
    }
}
}
printf("%10f\n",sum2);
return 0;
}