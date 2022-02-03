from math import gcd
from random import shuffle

n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

def random_submit():
    shuffle(ab)
    r_gcd, b_gcd = ab[0][0], ab[0][1]
    ans = r_gcd * b_gcd // gcd(r_gcd, b_gcd)

    for i in range(n - 1):
        num_r, num_b = r_gcd, b_gcd
        num_r = gcd(num_r, ab[i + 1][0])
        num_b = gcd(num_b, ab[i + 1][1])
        cnt_1 = num_r * num_b // gcd(num_b, num_r)

        num_r, num_b = r_gcd, b_gcd
        num_r = gcd(num_r, ab[i + 1][1])
        num_b = gcd(num_b, ab[i + 1][0])
        cnt_2 = num_r * num_b // gcd(num_b, num_r)
        if cnt_1 > cnt_2:
            r_gcd = gcd(r_gcd, ab[i + 1][0])
            b_gcd = gcd(b_gcd, ab[i + 1][1])
        else:
            r_gcd = gcd(r_gcd, ab[i + 1][1])
            b_gcd = gcd(b_gcd, ab[i + 1][0])
        
        ans = r_gcd * b_gcd // gcd(r_gcd, b_gcd)

    return ans

cnt = 0
for _ in range(100):
    cnt = max(cnt, random_submit())

print(cnt)