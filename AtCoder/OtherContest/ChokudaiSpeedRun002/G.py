n = int(input())
def gcd(n,m):
    ch = n%m
    while ch != 0:
        n = m
        m = ch
        ch = n%m
    return m
for _ in range(n):
    a,b = map(int,input().split())
    print(gcd(a,b))