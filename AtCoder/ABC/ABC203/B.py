#n = int(input())
n, k = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
for i in range(1, n + 1):
    for j in range(1, k + 1):
        ans += int(str(i) + "0" + str(j))
print(ans)