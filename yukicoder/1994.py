n = int(input())
s = [input() for _ in range(n)]

p = set()
for i in s:
    p.add(i)

for i in range(n):
    ans = 0
    for ind, j in enumerate(s[i]):
        t = [k for k in s[i]]
        for alpha in 'abcdefghijklmnopqrstuvwxyz':
            if j == alpha:
                continue
            t[ind] = alpha
            if "".join(t) in p:
                ans += 1
    
    print(ans)