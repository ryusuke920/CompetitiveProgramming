from itertools import  permutations

s, k = input().split()
k = int(k)
len_s = len(s)
t = sorted(list(s))

ans = []
for i in permutations(t, len_s):
    c = ''
    for j in range(len(s)):
        c += i[j]
    ans.append(c)

ans = sorted(list(set(ans)))

print(ans[k - 1])