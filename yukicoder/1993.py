n = int(input())
a = list(map(int, input().split()))

cnt = 1000
for i in range(n - 1):
    cnt *= (1000 - a[i]) / 1000

print(1000 - cnt)