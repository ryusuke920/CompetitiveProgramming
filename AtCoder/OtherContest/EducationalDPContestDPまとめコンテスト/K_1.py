n, k = map(int,input().split())
a = list(map(int,input().split()))

# dp[i] := 山がi個の時に、先手が勝てるかどうか
dp = [False] * (k + 1)

for i in range(k + 1):
    for j in range(n):
        if i - a[j] >= 0:
            if dp[i - a[j]] == False:
                dp[i] = True

if dp[k]:
    print("First")
else:
    print("Second")