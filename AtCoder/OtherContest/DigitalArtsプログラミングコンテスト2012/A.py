s = list(map(str,input().split()))
n = int(input())
ng = [input() for _ in range(n)]
ans = []
for i in range(len(s)):
    li = len(s[i])
    t = 0
    for j in range(n):
        lj = len(ng[j])
        if li != lj: continue
        Bool = True
        for k in range(li):
            if not (s[i][k] == ng[j][k] or ng[j][k] == "*"):
                Bool = False
        if Bool:
            t = 1
            ans.append("*" * li)
            break
    if t == 0:
        ans.append(s[i])

print(*ans)