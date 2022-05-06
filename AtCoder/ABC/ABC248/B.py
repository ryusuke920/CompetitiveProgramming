a, b, k = map(int, input().split())
ans = 0
while a < b:
    ans += 1
    a *= k
print(ans)