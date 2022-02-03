n,k = map(int,input().split())
# 解説AC
if 0 <= k <= n:
    print(k ** 3)
elif n <= k <= 2 * n:
    print(k ** 3 - 3 * (k - n) ** 3)
elif 2 * n <= k <= 3 * n:
    print(6 * n ** 3 - (3 * n - k) ** 3)
else:
    print(6 * n ** 3)