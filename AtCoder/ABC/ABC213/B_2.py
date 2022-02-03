def CC(A: list) -> list:
    "座標圧縮"
    B = {i: j for i, j in enumerate(sorted(set(A)))}
    return B

n = int(input())
a = list(map(int,input().split()))
num = CC(a)
#print(num)
print(a.index(num[n - 2]) + 1)