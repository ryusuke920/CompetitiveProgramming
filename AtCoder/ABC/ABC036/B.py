n = int(input())
s = [input() for i in range(n)]
ans = ""
for i in range(n):
    for j in range(n):
        ans += "".join(s[n-j-1][i])
for i in range(n):
    print(ans[n*i:n*(i+1)])