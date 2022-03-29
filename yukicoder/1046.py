n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
bool = False
for i in range(k):
    if a[i] >= 0:
        bool = True
    ans += max(0, a[i])

if bool:
    print(ans)
else:
    print(a[0])