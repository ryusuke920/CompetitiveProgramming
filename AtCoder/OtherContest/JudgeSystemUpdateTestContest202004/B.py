n = int(input())
a = [list(map(str,input().split())) for i in range(n)]
r = []
b = []
for i in range(n):
    if a[i][1] == "B":
        b.append(int(a[i][0]))
    else:
        r.append(int(a[i][0]))
r.sort()
b.sort()
ans = []
for i in range(len(r)):
    ans.append(r[i])
for i in range(len(b)):
    ans.append(b[i])
for i in range(len(ans)):
    print(ans[i])