from bisect import bisect_left
n, m = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
w = list(map(int,input().split()))
w.sort() # 必要ないけどまあ見やすさ意識ということで

front = [0] * (n // 2 + 2) # 両サイドに０の配列を追加
back = [0] * (n // 2 + 2) # 両サイドに０の配列を追加
for i in range(n // 2): # frontの処理
    front[i + 1] = h[2 * i + 1] - h[2 * i]
for i in range(n // 2, 0, -1): # backの処理
    back[i] = h[2 * i] - h[2 * i - 1]

for i in range(len(front) - 3): # front, backそれぞれの累積和をとっておく
    front[i + 2] += front[i + 1]
    back[-i - 3] += back[-i - 2]

ans = 10 ** 9
for i in range(m):# M回でのクエリのうち最小値を更新
    x = bisect_left(h, w[i])
    if x % 2 == 0: # frontが偶数の時
        num = front[x // 2] + (h[x] - w[i]) + back[x // 2 + 1]
    else: # frontが奇数の時
        num = front[x // 2] + (w[i] - h[x - 1]) + back[x // 2 + 1]
    ans = min(ans, num)
print(ans)