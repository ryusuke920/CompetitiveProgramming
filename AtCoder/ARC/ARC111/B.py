n = int(input())
a = [0] * n
b = [0] * n
left = [0] * (4 * 10 ** 5 + 1)
right = [0] * (4 * 10 ** 5 + 1)
both = [0] * (4 * 10 ** 5 + 1)
for i in range(n):
    a[i], b[i] = map(int,input().split())
    left[a[i] - 1] += 1
    right[b[i] - 1] += 1
    both[a[i] - 1] += 1
    both[b[i] - 1] += 1
for i in range(n):
    if both[a[i] - 1] <= both[b[i] - 1]:
        both[b[i] - 1] -= 1
    else:
        both[a[i] - 1] -= 1
ans = 0
for i in range((4 * 10 ** 5) + 1):
    if both[i] >= 1:
        ans += 1
print(ans)