#include<stdio.h>
int main(void){
int A[10]={0}, N=0, ch[10]={0};
for(int i=0;i<9;i++){
scanf("%d", &A[i]);
}
scanf("%d",&N);
int B[N];
for(int i=0;i<N;i++){
    scanf("%d", &B[i]);
}

for(int i=0;i<9;i++){
    for(int j=0;j<N;j++){
        if(A[i]==B[j]){
            ch[i]=1;
        }
    }
}
if(ch[0] && ch[1] && ch[2] == 1)printf("Yes\n");
else if(ch[3] && ch[4] && ch[5]== 1)printf("Yes\n");
else if(ch[6] && ch[7] && ch[8]== 1)printf("Yes\n");
else if(ch[0] && ch[3] && ch[6]== 1)printf("Yes\n");
else if(ch[1] && ch[4] && ch[7]== 1)printf("Yes\n");
else if(ch[2] && ch[5] && ch[8]== 1)printf("Yes\n");
else if(ch[0] && ch[4] && ch[8]== 1)printf("Yes\n");
else if(ch[2] && ch[4] && ch[6]== 1)printf("Yes\n");
else printf("No\n");
return 0;
}