n = int(input())
a = list(map(int,input().split()))
ans = [1] * 2
num = a[0]
for i in range(1, n):
    if num <= a[i]:
        ans[0] += 1
        num = a[i]
a = a[::-1]
num = a[0]
for i in range(1, n):
    if num <= a[i]:
        ans[0] += 1
        num = a[i]
print(max(ans[0], ans[1]))