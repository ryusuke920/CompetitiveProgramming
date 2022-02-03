n = int(input())
ans = 0
for i in range(1, 17): # the number of one
    for j in range(17): # the number of zero
        under = int("1" * i + "0" * j)
        top = int("1" * i + "9" * j)
        if under <= top and under <= n:
            ans += (min(n, top) - under + 1)

print(ans)