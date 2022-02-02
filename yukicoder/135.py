n = int(input())
x = list(map(int, input().split()))

ans = 10 ** 18
x.sort()
for i in range(n - 1):
    if x[i] == x[i + 1]: continue
    ans = min(ans, abs(x[i + 1] - x[i]))
print(ans) if ans != 10 ** 18 else print(0)