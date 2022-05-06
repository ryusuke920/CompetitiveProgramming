n, k = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(n)]
now = 0
bef = 0
dec = []
for i in range(n):
    t, y = q[i]
    bef = now
    if t == 1:
        now = y
    elif t == 2:
        now += y
    dec.append(now - bef)

for i in range(len(dec)):
    dec[i] *= -1

dec.sort(reverse=True)
for i in range(min(k, len(dec))):
    if dec[i] >= 0:
        now += dec[i]
print(now)