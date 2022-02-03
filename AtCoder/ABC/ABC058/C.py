from collections import Counter
n = int(input())
x = []
for i in range(n):
    s = input()
    t = Counter(s)
    x.append(t)
ans = ""
for i in "abcdefghijklmnopqrstuvwxyz":
    tmp = []
    for j in x:
        tmp.append(j[i])
    ans += i*min(tmp)
print(ans)