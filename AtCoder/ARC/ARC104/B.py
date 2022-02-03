n,s = map(str,input().split())
n = int(n)
cnt = 0
for i in range(n):
    at = cg = 0
    for j in range(i,n):
        if s[j] == "A":
            at += 1
        elif s[j] == "G":
            cg += 1
        elif s[j] == "T":
            at -= 1
        else:
            cg -= 1
        if at == 0 and cg == 0:
            cnt += 1
print(cnt)