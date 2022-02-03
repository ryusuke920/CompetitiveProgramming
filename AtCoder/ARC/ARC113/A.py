k = int(input())
ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        if i * j > k:
            break
        ans += k // i // j
print(ans)