n = int(input())
a = sorted(list(map(int,input().split())))

# 累積和を取る
wa = [0] * n
wa[0] = a[0]
for i in range(n - 1):
    wa[i + 1] += wa[i] + a[i + 1]

ans = 0
for i in range(n - 1):
    if a[i + 1] > 2 * wa[i]:
        ans = i + 1
print(n - ans)