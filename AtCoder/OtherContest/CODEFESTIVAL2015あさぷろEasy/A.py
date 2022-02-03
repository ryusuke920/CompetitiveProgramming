n = int(input())
ans = 0
for i in range(500):
    if i * i >= n:
        ans = i * i - n
        break
print(ans)