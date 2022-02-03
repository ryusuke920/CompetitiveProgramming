def is_ok(num: int):
    # 条件を満たすかどうか？問題ごとに定義
    if a * num + b * len(str(num)) <= x:
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

a, b, x = map(int,input().split())
INF = 10 ** 9 + 1
l, r = -1, INF
ans = binary_search(l, r)
if ans == -1:
    print(0)
else:
    print(ans)