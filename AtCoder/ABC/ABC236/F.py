from itertools import product

n = int(input())
c = list(map(int, input().split()))
c.sort()

def dp(k: int) -> bool:
    '辛さkが作れるかどうか'

ans = 10 ** 18
s = []
for i in s:
    bool = True
    for i in range(2 ** n - 1):
        if dp[i]: continue
        bool = False
    
    if bool:
        break
    else:
        s.append(i)

print(s)
print(sum(s))