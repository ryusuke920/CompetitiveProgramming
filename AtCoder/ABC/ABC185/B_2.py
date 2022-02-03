n, m , t = map(int, input().split())

cnt = n
now = 0
for i in range(m):
    a, b = map(int, input().split())
    dist = a - now
    cnt -= dist
    if cnt <= 0:
        exit(print('No'))
    
    cnt += b - a
    cnt = min(n, cnt)
    now = b
if now + cnt > t:
    print('Yes')
else:
    print('No')