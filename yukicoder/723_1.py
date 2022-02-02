from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))

d_1 = defaultdict(int)
d_2 = defaultdict(int)
for i in a:
    d_1[i] += 1
    d_2[i] += 1

ans = 0
'''
k + t = x
kがv個、tがd_2[t]個 -> v * d_2[t] (k != t)
kがv個、tがd_2[t]個 -> v ** 2 (k == t)
'''
for k, v in d_1.items():
    t = x - k
    if t < 0: continue
    ans += v * d_2[t]

print(ans)