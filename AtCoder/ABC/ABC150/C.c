#include<stdio.h>
int main(void){
int N, P[10], Q[10], a=0, b=0;
scanf("%d", &N);
for(int i=1; i<=N; i++){
scanf("%d",&P[i-1]);
}
for(int i=1; i<=N; i++){
scanf("%d",&Q[i-1]);
}
for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
       if(P[i+j] % (N-j) != 0){
     a+=N;
    }
  }
}
for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
       if(Q[i+j] % (N-j) != 0){
     b+=N;
    }
  }
}
if(a-b>0){
printf("%d",a-b);
}else{
printf("%d",b-a);
}
return 0;
}