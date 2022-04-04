def f(a: int, b: int) -> int:
    return a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3


def binary_search(left: int, right: int, a: int) -> int:
    while right - left > 1:
        b = (left + right) // 2
        if f(a, b) < n:
            left = b
        else:
            right = b

    return right

n = int(input())

INF = 10 ** 18 + 1
for a in range(1, int(n ** (1/3)) + 1):
    l, r = -1, INF
    cnt = binary_search(l, r, a)
    print(f(a, cnt))
    break