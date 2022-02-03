n = int(input())
a = [set() for _ in range(n)]
for i in range(n):
    A = list(input())
    for j in A:
        a[i].add(j)

ans = []
for i in range(n // 2):
    if a[i] & a[-1 - i]:
        ans.append(list(a[i] & a[-1 - i])[0])

if n % 2 == 0:
    if len(ans) == n // 2:
        ans += ans[::-1]
        print(*ans, sep="")
    else:
        print(-1)
elif n % 2 == 1:
    ans.append(list(a[n // 2])[0])
    if len(ans) == (n + 1) // 2:
        for i in range(n // 2):
            ans.append(ans[-2 - i])
        print(*ans, sep="")
    else:
        print(-1)