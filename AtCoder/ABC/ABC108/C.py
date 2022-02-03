n, k = map(int,input().split())
ans = 0
p = n // k
q = (n + k // 2) // k
if k % 2 == 1:
    ans += p ** 3
else:
    ans += p ** 3 + q ** 3
print(ans)