n = int(input())
p = list(map(int,input().split()))
num = [0]*(200001)
ans = 0
for i in range(n):
    x = p[i]
    num[x] = 1
    while num[ans] == 1:
        ans += 1
    print(ans)