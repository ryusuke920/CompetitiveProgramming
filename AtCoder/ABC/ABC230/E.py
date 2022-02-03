n = int(input())
ans = 0
for i in range(1, int(n ** 0.5) + 1):
    ans += i * ((n // i) - n // (i + 1))

for i in range(1, int(n // int(n ** 0.5 + 1) + 1)):
    ans += n // i

print(ans)