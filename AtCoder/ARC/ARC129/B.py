def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    if 1:
        return True
    else:
       return False

def binary_search(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid
    return left # Trueの方を返す？
from math import ceil
INF = 10 ** 18
l, r = -1, INF
n = int(input())
lr = [list(map(int,input().split())) for _ in range(n)]
left_ma = 0
right_mi = INF
for i in range(n):
    left_ma = max(left_ma, lr[i][0])
    right_mi = min(right_mi, lr[i][1])

    if right_mi <= left_ma:
        print(ceil((left_ma - right_mi) / 2))
    else:
        print(0)