n = int(input())
ans = 0
num = []
for i in range(max(n - 153, 1), n):
    x = i
    cnt = x
    while x > 0:
        cnt += x % 10
        x //= 10
    if cnt == n:
        ans += 1
        num.append(i)
print(ans)
for i in range(ans):
    print(num[i])