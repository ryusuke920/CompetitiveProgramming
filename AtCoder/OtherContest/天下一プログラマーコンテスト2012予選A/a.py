n = int(input())
an2 = 1
an1 = 1
ans = 0
if n == 0 or n == 1:
    print(1)
else:
    for i in range(n-1):
        an = an2 + an1
        an1 = an2
        an2 = an
    print(an)