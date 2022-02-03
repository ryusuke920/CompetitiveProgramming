# これの優しいバージョン(ABC164-D)
n, p = map(int,input().split())
s = list(map(int,list(input())))

if p == 2 or p == 5: # 右端が p になっていれば良い
    ans = 0
    for i in range(len(s)):
        if s[i] % p == 0:
            ans += i + 1
else:
    s = s[::-1]
    s = [0] + s
    for i in range(len(s) - 1):
        s[i + 1] *= pow(10, i, p)
        s[i + 1] %= p

    # 累積和を取る
    s[1] %= p
    for i in range(len(s) - 2):
        s[i + 2] += s[i + 1]
        s[i + 2] %= p

    cnt = [0] * p
    for i in range(len(s)):
        cnt[s[i]] += 1

    ans = 0
    for i in range(p):
        ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)