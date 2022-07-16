from random import randint

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

ans = set()
for _ in range(k):
    a, b, c, d = [randint(-10 ** 4, 10 ** 4) for _ in range(4)]
    ans.add((a, b, c, d))

print(k)
for i in ans:
    print(*i)