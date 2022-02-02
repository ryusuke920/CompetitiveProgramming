from collections import defaultdict

n = int(input())
x = sorted(list(map(int, input().split())))

d = defaultdict()

# dp[i] := Sの末尾をiとした時に作成できる長さの最大値
dp = [0] * max(x)
print(max(dp))