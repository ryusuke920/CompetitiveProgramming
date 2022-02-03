def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(set(A))}
    return B

from collections import Counter
n = int(input())
#x, y = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
x = Counter(a).most_common()
#print(x)
num = 0
for i in range(len(x)):
    num += (x[i][1] - 1) * x[i][1] // 2

print(n * (n - 1) // 2 - num)