N=input()
S=list(map(int,input().split()))
for a in range(1, 335):
    for b in range(1, 335):
        square=4*a*b+3*a+3*b
        while square in S:
            S.remove(square)
print(len(S))