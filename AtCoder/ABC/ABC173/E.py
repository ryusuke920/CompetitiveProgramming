n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
p = []
for i, j in enumerate(a):
    if j >= 0:
        p.append((j, j, i))
    elif j < 0:
        p.append((-j, j, i))

p.sort(key=lambda x: x[0], reverse=True)
ans = 1
minus, plus = [], []
is_minus, is_plus = False, False
for i in range(k):
    ans *= p[i][1]
    if p[i][1] < 0:
        minus.append((i, p[i][1]))
        is_minus = True
    if p[i][1] > 0:
        plus.append((i, p[i][1]))
        is_plus = True
    ans %= mod
#print(*p, sep='\n')
minus.sort(key=lambda x: x[1], reverse=True)
plus.sort(key=lambda x: x[1])
#print('num=',num)
if len(minus) % 2 == 0:
    print(ans)
elif len(minus) % 2 == 1:
    '''
    全体が負になる
    1. 正にする <=> k+1以降に（最大の）負が存在する <=> 最小の正を消す <=> 負を追加する
    2. 正にする <=> k+1以降に（最大の）正が存在する <=> 最小の負を消す <=> 正を追加する
    3. 正にするのが不可能 <=> 絶対値で昇順にソート <=> 小さいものから k
    '''
    # 現在 minus <=> k + 1 以降に +, - があるか探す
    x, y = [], [] # x := +, y:= -
    cnt = []
    for i in range(k, n):
        if p[i][1] > 0:
            x.append((p[i][1], i))
        if p[i][1] < 0:
            y.append((p[i][1], i))
    x.sort(key=lambda t: t[0], reverse=True)
    u = []
    if len(x) and is_minus: # 2.
        ans = 1
        for i in range(k):
            if i != minus[0][0]:
                ans *= p[i][1]
                ans %= mod
            else:
                u.append(minus[0][1])
        ans *= x[0][0]
        u.append(x[0][0])
        ans %= mod
        cnt.append(ans)
    y.sort(key=lambda t: t[0])
    t = []
    if len(y) and is_plus: # 1.
        ans = 1
        for i in range(k):
            if i != plus[0][0]:
                ans *= p[i][1]
                ans %= mod
            else:
                t.append(plus[0][1])
        ans *= y[0][0]
        t.append(y[0][0])
        ans %= mod
        cnt.append(ans)

    # minusになるので小さいのを選ぶ
    if len(cnt) == 0:
        p.sort(key=lambda x: x[0])
        ans = 1
        for i in range(k):
            ans *= p[i][1]
            ans %= mod
        cnt.append(ans)
        print(max(cnt))
    else:
        if len(cnt) == 1:
            print(cnt[0])
        else:
            print(cnt[1]) if u[1] * t[0] < u[0] * t[1] else print(cnt[0])

'''
7 5
10 20 30 -11 2 4 0
--- 48000


'''