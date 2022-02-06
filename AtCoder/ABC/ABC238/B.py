n = int(input())

now = 0
a = list(map(int,input().split()))

num = [0] * 360
num[0] = 1

for i in range(n):
    now = (now + a[i]) % 360
    num[now] = 1

ans = 1
cnt = 1
for i in range(360):
    if num[i] == 0:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

print(max(ans, cnt))