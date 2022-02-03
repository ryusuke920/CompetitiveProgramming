n = int(input())
a = list(map(int,input().split()))
num = 0
for i in range(n):
    num ^= a[i]

ans = []
for i in range(n):
    ans.append(num ^ a[i])

print(*ans)