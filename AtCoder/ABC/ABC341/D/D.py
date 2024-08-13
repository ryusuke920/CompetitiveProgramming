from math import lcm
def check(mid: int) -> True:
    "mid 以下で条件を満たすのが k 個以上あるかどうか"
    cnt = (mid // n) + (mid // m) - (mid // lcm_) * 2
    #print(mid, cnt, lcm_)

    if cnt >= k:
        return True
    else:
       return False

def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    return right


n, m, k = map(int, input().split())
lcm_ = lcm(n, m)
l, r = 0, 10**18
ans = binary_search(l, r)
print(ans)