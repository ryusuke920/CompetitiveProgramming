#include<stdio.h>
int main(void){
int N ,T,A,sum;
scanf("%d%d%d",&N,&T,&A);
int H[N];
double ch[N];
for(int i=0;i<N;i++) scanf("%d",&H[i]);
double x[N],ans=500000;
for(int j=0;j<N;j++){
     ch[j]=T-H[j]*0.006;
/*    printf("A-ch[j]:%d\n",A-ch[j]);
    printf("A-ch[j]:%lf\n",A-ch[j]);
     printf("A-ch[j]:%d\n",(double)abs(A-ch[j]));
      printf("A-ch[j]:%lf\n",abs(A-ch[j]));
      */
}

for(int k=0;k<N;k++){
    if((double)abs(A-ch[k])<ans){
        ans=abs(A-ch[k]);
        sum=k+1;
        printf("k:%d",k);
    }
}
printf("%d\n",sum);
return 0;
}