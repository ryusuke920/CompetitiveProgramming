n = int(input())
a = list(map(int,input().split()))

def CC(A: list) -> list:
    "座標圧縮"
    B = {i + 1: j for i, j in enumerate(sorted(set(A)))}
    return B

print(a.index(CC(a)[n - 1]) + 1)