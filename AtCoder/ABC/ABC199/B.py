n = int(input())
#x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = cnt = 0
num = [True] * 1000
for i in range(n):
    for j in range(1, 1001):
        if a[i] <= j and j <= b[i]: continue
        num[j - 1] = False

for i in range(len(num)):
    if num[i]:
        ans += 1
print(ans)