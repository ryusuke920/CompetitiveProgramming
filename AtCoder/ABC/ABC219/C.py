from collections import defaultdict

x = input()
d = defaultdict(int)

for i in range(len(x)):
    d[x[i]] = i

n = int(input())
a = []
for i in range(n):
    s = input()
    a_list = []
    for j in range(len(s)):
        a_list.append(d[s[j]])
    a.append(a_list)

a.sort()

for i in range(n):
    ans = ''
    for j in range(len(a[i])):
        ans += x[a[i][j]]
    print(ans)