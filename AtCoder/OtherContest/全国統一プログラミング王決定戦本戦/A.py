n = int(input())
a = list(map(int,input().split()))
ans = [0] * n
for i in range(n):
    cnt = sum(a[:i + 1])
    print(i,cnt)
    for j in range(n - i - 1):
        cnt += a[j + n - i - 1] - a[j]
    