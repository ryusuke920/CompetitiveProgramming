ans = 0.0
n = int(input())
for i in range(1, n):
    ans += n / (n - i)
print(ans)