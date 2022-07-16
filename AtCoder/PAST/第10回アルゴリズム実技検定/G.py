def f(x: int) -> int:
    return a * x ** 5 + b * x + c

def binary_search(left: int, right: int) -> int:
    while right - left > 10 ** -12:
        mid = (left + right) / 2
        if f(mid) <= 0:
            left = mid
        else:
            right = mid

    return left

l, r = -1, 10 ** 18
a, b, c = map(int, input().split())
print(binary_search(l, r))

