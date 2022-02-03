A,B,C,K = map(int,input().split())
if A + B + C == K:
    print(A - C)
elif (K >= A + B) and (K < A + B + C)  :
    print(A - K + A + B)
elif (K >=A and K < A + B):
    print(A)
else:
    print(K)