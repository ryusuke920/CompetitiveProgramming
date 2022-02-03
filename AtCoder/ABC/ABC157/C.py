n,m = map(int,input().split())
s = [0]*m
c = [0]*m
ans = -1
for i in range(m):
    s[i],c[i] = map(int,input().split())
for i in range(10**n):
    a = str(i)
    if len(a) != n:
        continue
    if all(a[s[j]-1] == str(c[j]) for j in range(m)):
        ans = i
        break
print(ans)