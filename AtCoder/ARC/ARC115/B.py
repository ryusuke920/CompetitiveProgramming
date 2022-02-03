import sys
input = sys.stdin.readline
n = int(input())
c = [list(map(int,input().split())) for _ in range(n)]

a = [0] * n
b = [0] * n

for i in range(n):
    a[i] = c[i][0] - c[0][0]
    b[i] = c[0][i] - c[0][0]
    for j in range(n - 1):
        if a[i] != c[i][j + 1] - c[0][j + 1] or b[i] != c[j + 1][i] - c[j + 1][0]:
            exit(print("No"))

if c[0][0] + min(a) + min(b) < 0:
    exit(print("No"))

mi_a = min(a)

a = [i - mi_a for i in a]
b = [i + c[0][0] + mi_a for i in b]
print("Yes")
print(*a)
print(*b)