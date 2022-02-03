n = int(input())
ans = 1
for i in range(n):
    ans += 5**(i+1)
print(ans)