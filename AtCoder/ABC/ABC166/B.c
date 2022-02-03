#include<stdio.h>
int main(void){
int N , K;
scanf("%d%d",&N,&K);
int d[1000], A[10000][d[1000]];
for(int i=0;i<K;i++){
    scanf("%d",d[i]);
    for(int j=0;j<d[i];j++){
        scanf("%d",&A[i][j]);
        printf("i=%d,j=%d‚ÌŽžA[i][j]=%d\n",i,j,A[i][j]);
    }
}
int ch[10000];
for(int x=1;x<=N;x++){
    for(int i=0;i<K;i++){
        for(int j=0;j<K;j++){
            if(x==A[i][j]) ch[x]++;
        }
    }
}
int ans=0;
for(int x=1;x<=N;x++){
    if(ch[x]==0) ans++;
}
printf("ans:%d\n", ans);
return 0;
}