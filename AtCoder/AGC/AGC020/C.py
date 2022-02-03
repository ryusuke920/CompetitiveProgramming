n = int(input())
a = list(map(int, input().split()))
dp = 1
for i in range(n):
    dp |= dp << a[i]
binary = bin(dp)[2:][::-1]
#print(binary)
ans = []
for i in range(len(binary)):
    if binary[i] == "1":
        ans.append(i)
#print(ans)
print(ans[len(ans) // 2])