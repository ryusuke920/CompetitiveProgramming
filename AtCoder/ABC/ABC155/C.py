from collections import Counter
n = int(input())
s = [str(input()) for _ in range(n)]
num = Counter(s)
ans = []
ma = max(num.values())
for i in sorted(num):
    if num[i] == ma:
        print(i)