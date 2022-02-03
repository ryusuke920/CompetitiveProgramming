n = int(input())
ans = [0] * n
for _ in range(n - 1):
    a, b = map(int,input().split())
    ans[a - 1] += 1
    ans[b - 1] += 1

for i in ans:
    if i == n - 1:
        exit(print("Yes"))

print("No")