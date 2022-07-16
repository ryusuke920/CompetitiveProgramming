def check(k: int) -> bool:

    cost = 0

    for i in range(n):
        if p[i] > k:
            cost += ((p[i] - k) // b)
        elif p[i] < k:
            num = (a + (k - p[i]) - 1) // a
            cost -= num

    return cost >= 0


def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left

n, a, b = map(int, input().split())
p = list(map(int, input().split()))

ans = binary_search(-1, 10 ** 18)
print(ans) if ans != -1 else print(min(p))