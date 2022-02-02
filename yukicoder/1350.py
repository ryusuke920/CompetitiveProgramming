from math import gcd

a, b, k = map(int, input().split())

'''
答えをkとする
<=> k以下の自然数でa, bの倍数がk個ある
'''

l, r = 0, 10 ** 18 + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = mid // a + mid // b - mid // (a * b // gcd(a, b))
    if cnt >= k:
        r = mid
    else:
        l = mid

print(r)