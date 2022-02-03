n, m = map(int,input().split())
num = [0] * m 
cnt = 0
for i in range(n):
    l, r, s = map(int,input().split())
    num[l - 1] += s # 0 index
    if r <= m - 1:
        num[r] -= s # 0index
    cnt += s

for i in range(1, m):
    num[i] += num[i - 1]
print(cnt - min(num))