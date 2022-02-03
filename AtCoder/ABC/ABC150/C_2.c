#include<stdio.h>
void cha(int n,int a1[],int c1[]){
for(int i=0;i<n;i++){
        c1[i]=a1[i];
    for(int j=0;j<i;j++){
            if(a1[i]>a1[j]){
                c1[i]--;
            }   
        }
    }
}

int main(void){
    int N;
    int a[10];
    int b[10];
    int ch[10];
    int nm=1;
    int L1=1;
    int L2=1;

    scanf("%d",&N);
for(int i=0;i<N;i++){
    scanf("%d",&a[i]);
}
for(int i=0;i<N;i++){
    scanf("%d",&b[i]);
}

for(int i=1;i<=N;i++){
    nm=nm*i;
}

cha(N,a,ch);

for(int i=0;i<N-1;i++){
    nm=nm/(N-i);
    L1=L1+nm*(ch[i]-1);
}

nm=1;

for(int i=1;i<=N;i++){
    nm=nm*i;
}
cha(N,b,ch);

for(int i=0;i<N-1;i++){
    nm=nm/(N-i);
     L2=L2+nm*(ch[i]-1);


}

if(L1>L2){
    printf("%d\n",L1-L2);
  }else{
    printf("%d\n",L2-L1);
}

return 0;
}

