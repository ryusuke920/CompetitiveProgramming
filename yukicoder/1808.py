n, m = map(int, input().split())
a = list(map(int, input().split()))

'''
<=> 二分探索で k にできるかどうか
<=> bool で判断する
<=> i番目までで合計がik個あればTrue
<=> Trueならば答えは floor(k/m)
'''

def is_ok(k: int):
    # i番目までの合計を ki 以上に維持できるかどうか
    bool = True
    cnt = 0
    for i in range(n):
        cnt += a[i]
        if cnt >= k * (i + 1): continue
        bool = False

    if bool:
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
print(binary_search(l, r) // m)