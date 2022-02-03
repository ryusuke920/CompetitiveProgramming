ans = 0
d = list(map(int, input().split()))
j = list(map(int, input().split()))
for i in range(7):
    ans += max(d[i], j[i])

print(ans)