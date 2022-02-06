ans = 0
for i in range(5):
    n = int(input())
    ans += max(n, 40)
print(ans//5)