from bisect import bisect_left

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

INF = 10 ** 18
l, r = -1, INF
print(binary_search(l, r))

q = int(input())
num = []
v = 0
for i in range(q):
    t, x = map(int,input().split())
    if t == 1:
        num.append(x)
    else:
        print(i,num)
        print(num[x + v - 1])
        v += 1