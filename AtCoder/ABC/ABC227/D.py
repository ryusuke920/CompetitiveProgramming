def count(n: int, a: list, p: int) -> int:
    num = 0
    for i in range(n):
        num += min(a[i], p)
    return num

def binary_search(left: int, right: int, n: int, a: list) -> int:
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if count(n, a, mid) >= k * mid:
            left = mid
        else:
            right = mid
    return left

INF = 10 ** 18
l, r = -1, INF

n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

ans = binary_search(l, r, n, a)
print(ans)