n = int(input())
s = str(input())
ans = 0
count = 0
ch = []
for i in range(1,n):
    a = s[:i]
    b = s[i:]
    for j in range(i):
        if a[j] in b and a[j] not in ch:
            count += 1
        ch.append(a[j])
    ans = max(count,ans)
    count = 0
    ch = []
print(ans)