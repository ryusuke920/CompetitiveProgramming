n, h, m, t = map(int,input().split())
num = (n  - 1) * t
h += (num // 60)
h %= 24
m += (num % 60)
if m >= 60:
    h += 1
    m -= 60
if h == 24:
    h = 0
print(h)
print(m)