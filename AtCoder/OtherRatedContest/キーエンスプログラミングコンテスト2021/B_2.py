n, k = map(int,input().split())
a = list(map(int,input().split()))
num = [0] * (max(a) + 1)
for i in range(n):
    num[a[i]] += 1
mi = num[0]
for i in range(len(num) - 1):
    if mi > num[i + 1]:
        mi = num[i + 1]
    num[i + 1] = mi
num = num[::-1]
cnt = 0 # 個数
ans = 0 # 答え
i = 0
le = len(num)
while True:
    while True: # いつまでいれるか
        if num[i] <= cnt:
            i += 1
            break
        ans += le - i
        cnt += 1
    if i >= len(num) or cnt >= k:
        break
print(ans)