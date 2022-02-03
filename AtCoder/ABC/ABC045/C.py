#bit全探索
s = input()
ans = 0
for i in range(2**(len(s)-1)):
    t = 0
    for j in range(len(s)-1):
        if (i >> j)&1:
            ans += int(s[t:j+1])
            t = j+1
    ans += int(s[t:])
print(ans)