n,m = map(int,input().split())
s = [input() for _ in range(n)]
odd = 0
for i in range(n):
    if s[i].count("1") % 2 == 0:
        odd += 1
print(odd * (n - odd))