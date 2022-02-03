n, m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))

if len(set(t)) == 1 and s[0] == t[0]:
    print(m)
elif len(set(s)) == 1:
    print(-1)
else:
    ind = 0
    while s[0] == s[ind] and s[0] == s[-ind]:
        ind += 1

    ans = m
    for i in range(m - 1):
        if t[i] != t[i + 1]:
            ans += 1
    
    if s[0] == t[0]:
        print(ind + ans - 1)
    else:
        print(ind + ans)