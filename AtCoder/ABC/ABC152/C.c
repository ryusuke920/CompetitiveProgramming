#include<stdio.h>
int main(void){
long int N ,n[100010]={0};
int ch[100010]={0}, ch2=0;
scanf("%ld", &N);
for(int i=0;i<N;i++){
    scanf("%ld",&n[i]);
}
for(int i=0;i<N;i++){
    for(int j=0;j<N && j<=i;j++){
        if(n[i]<=n[i-j]){
        ch[i]+=1;//true
    }
  }
}
for(int i=0;i<N;i++){
    if(ch[i]==i+1){
    ch2++;
    }
}
printf("%d\n",ch2);
return 0;
}