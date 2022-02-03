n, k = map(int,input().split())
x = list(map(int,input().split()))

from collections import defaultdict
d = defaultdict(int)
for i in range(n):
    d[x[i]] = i + 1

from heapq import heapify, heappush, heappop
a = []
heapify(a)

# 基準となる全体のうちのK番目までを入れる
for i in range(k):
    heappush(a, -x[i])
ans = heappop(a)
print(d[-ans])
heappush(a, ans)

for i in range(k, n):
    # 比較するための現段階のK位の人
    cnt = heappop(a)
    if -cnt >= x[i]:
        # 現段階でのK番目の方が今回の方よりも数が大きい
        # <=> 今回の方が良い順位
        # <=> 最下位を入れ替える
        heappush(a, -x[i])
    elif -cnt < x[i]:
        # 現段階でのK番目の方が今回の方よりも数が小さい
        # <=> 今回の方が悪い順位
        # <=> 何もしない
        # <=> 元に戻す
        heappush(a, cnt)

    ans = heappop(a)
    print(d[-ans])
    heappush(a, ans)