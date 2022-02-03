from bisect import bisect_right
n, k = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

"""
二分探索を使用する
下からK番目をX <=> X以下の数がK個以上ある
Xが大きくなる <=> K個以上は増えていくので単調増加
"""

def is_ok(x: int) -> bool:
    cnt = 0
    for i in range(n):
        t = bisect_right(b, x // a[i])
        cnt += t

    if cnt >= k:
        return True
    else:
        return False

def binary_search(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right

INF = 10 ** 20
l, r = -1, INF
print(binary_search(l, r))