from re import T


n, d = map(int, input().split())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

l, r = 0, 10 ** 9 + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    for i in range(n):
        cnt += v[i] * mid
    
    if cnt >= d:
        r = mid
    else:
        l = mid

print(r)