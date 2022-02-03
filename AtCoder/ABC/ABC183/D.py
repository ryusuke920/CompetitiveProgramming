n,w = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]
ma = 0
for i in range(n):
    ma = max(ma,s[i][1])

num = [0]*(ma+1)
for i in range(n):
    num[s[i][0]] += s[i][2]
    if s[i][1]-1 < ma:
        num[s[i][1]] -= s[i][2]

ans = 0
for i in range(len(num)):
    ans += num[i]
    if ans > w:
        print("No")
        exit()
print("Yes")