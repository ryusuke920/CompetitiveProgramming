n = int(input())
s = [int(input()) for  _ in range(n)]
ans = sum(s)
s.sort()
if ans%10 != 0:
    print(ans)
else:
    t = []
    for i in range(n):
        if s[i]%10 != 0:
            t.append(s[i])
    if len(t) == 0:
        print(0)
    else:
        print(ans-t[0])