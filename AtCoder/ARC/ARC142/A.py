from collections import defaultdict

def f(x: int) -> bool:
    if not (1 <= x <= n):
        return False

    ans = [x]
    d = defaultdict(int)
    d[x] += 1
    while True:
        x = int(str(x)[::-1])
        d[x] += 1
        ans.append(x)
        if d[x] >= 2:
            break

    if len(ans):
        p = min(list(set(ans)))
        if p == k:
            return True
        else:
            return False
    else:
        return False

n, k = map(int, input().split())
ans = []

if f(k):
    ans.append(k)
    while True:
        num = ans[-1]
        if f(num * 10):
            ans.append(num * 10)
        else:
            break

if f(int(str(k)[::-1])):
    ans.append(int(str(k)[::-1]))
    while True:
        num = ans[-1]
        if f(num * 10):
            ans.append(num * 10)
        else:
            break

print(len(set(ans)))