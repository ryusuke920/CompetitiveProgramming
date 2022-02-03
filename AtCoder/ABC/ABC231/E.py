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

    return left

INF = 10 ** 18
l, r = -1, INF

n, x = map(int,input().split())
a = list(map(int,input().split()))
max_use = [1] * n
for i in range(n - 1):
    max_use[i + 1] = a[i + 1] // a[i]
print(max_use)

print(binary_search(l, r))