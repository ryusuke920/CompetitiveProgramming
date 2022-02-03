# dp[i桁目まで確定した時][既にn未満確定?][4か9が出てきたか?]
def solve(s: str):
    l = len(s)
    dp = [[[0] * 2 for _ in range(2)] for _ in range(30)]
    dp[0][0][0] = 1
    
    for i in range(l):
        for flag in range(2):
            num = 9 if flag else int(s[i])
            for j in range(2):
                for k in range(num + 1):
                    if (k == 4 or k == 9) and j == 0:
                        dp[i + 1][flag or k < num][j + 1] += dp[i][flag][j]
                    else:
                        dp[i + 1][flag or k < num][j] += dp[i][flag][j]
    
    return dp[l][0][1] + dp[l][1][1]

a, b = map(int,input().split())
print(solve(str(b)) - solve(str(a - 1)))