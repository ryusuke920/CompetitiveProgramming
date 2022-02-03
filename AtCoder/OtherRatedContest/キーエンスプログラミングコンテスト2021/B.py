n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
num = [0] * (max(a) + 1)
for i in range(n):
    num[a[i]] += 1

ans = 0
score = [0] * len(num)
score[0] = num[0]
mi = num[0]
for i in range(len(num) - 1):
    if mi > num[i + 1]:
        mi = num[i + 1]
    score[i + 1] = min(mi, num[i + 1])
score = score[::-1]
roop = 1
le = len(score)
i = 0
while True:
    while True:
        if score[i] < roop:
            i += 1
            break
        ans += le - i
        roop += 1
    if roop == k + 1 or i >= len(score):
        break
print(ans)