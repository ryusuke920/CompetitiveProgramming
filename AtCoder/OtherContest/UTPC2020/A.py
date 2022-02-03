n, l = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

# 初期値を k で達成できるかどうかで２分探索
l, r = -1, 10 ** 9 + 1
while r - l > 1:
    mid = (l + r) // 2
    power = mid - a[0][1] # 気力
    bool = True # 途中で0未満になるとFalse

    for i in range(n - 1):
        power += a[i + 1][0] - a[i][0]
        power = min(power, mid)
        power -= a[i + 1][1]
        if power < 0:
            bool = False

    if bool:
        r = mid
    else:
        l = mid

print(r)