#DP (Dynamic Programming)
n = int(input())
a = list(map(int,input().split()))
dp = [0,abs(a[0]-a[1])]
for i in range(n-2):
    dp.append(min(dp[-2]+abs(a[i]-a[i+2]),dp[-1] + abs(a[i+1]-a[i+2])))
print(dp[-1])