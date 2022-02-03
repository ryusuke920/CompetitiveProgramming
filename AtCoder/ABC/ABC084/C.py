# 解説AC
n = int(input())
c = [0] * (n - 1) # 次までにかかる時間
s = [0] * (n - 1) # 出発時刻
f = [0] * (n - 1) # 間隔
for i in range(n-1):
    c[i], s[i], f[i] = map(int,input().split()) # かかる時間・開通式・電車間

for i in range(n):
    ans = 0
    for j in range(i, n - 1):
        if ans < s[j]:
            ans = s[j]
        elif ans % f[j] != 0:
            ans += f[j] - ans % f[j]
        ans += c[j]
    print(ans)