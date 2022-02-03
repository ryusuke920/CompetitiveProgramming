def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    num = a * arg + b * len(str(arg))
    if num <= x:
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
        print(left,right)
    
    return (left,right)

a, b, x = map(int,input().split())
INF = x + 1
l, r = -1, INF
ans = binary_search(l, r)
if ans[0] != -1:
    print(min(ans[0], 10 ** 9))
else:
    print(0)