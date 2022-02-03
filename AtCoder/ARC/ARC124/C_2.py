#素因数分解、計算量はO(√N)
def divisor(n):
    cd = []
    i = 1
    while i*i <= n:
        if n%i==0:
            cd.append(i)
            if i != n//i:
                cd.append(n//i)
        i += 1
    return cd
N = int(input())
A,B = [0]*N,[0]*N
from math import gcd
for i in range(N):
    A[i],B[i] = map(int, input().split())
cds1 = divisor(A[0])
cds2 = divisor(B[0])
ans = 0
for cd1 in cds1:
    for cd2 in cds2:
        for i in range(N):
            if (A[i]%cd1!=0 or B[i]%cd2!=0) and (A[i]%cd2!=0 or B[i]%cd1!=0): break
        else:
            ans = max(ans, cd1*cd2//gcd(cd1,cd2))
print(ans)