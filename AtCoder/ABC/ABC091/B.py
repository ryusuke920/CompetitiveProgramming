n = int(input())
s = [str(input()) for i in range(n)]
m = int(input())
t = [str(input()) for i in range(m)]
used = []
for i in range(n):
    if s[i] not in used:
        used.append(str(s[i]))
for j in range(m):
    if t[j] not in used:
        used.append(str(t[j]))

ans = [0]*len(used)
for i in range(len(used)):
    for j in range(n):
        if s[j] == used[i]:
            ans[used.index(used[i])] += 1

for i in range(len(used)):
    for j in range(m):
        if t[j] == used[i]:
            ans[used.index(used[i])] -= 1
if max(ans) >= 0:
    print(max(ans))
else:
    print(0)