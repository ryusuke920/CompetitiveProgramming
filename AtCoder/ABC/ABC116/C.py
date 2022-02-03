n = int(input())
h = list(map(int,input().split()))
ans = 0
tmp = 0
for i in range(len(h)):
    if tmp < h[i]:
        ans += h[i] - tmp
    tmp = h[i]
print(ans)