def reflect(a: int, b: int):
    if a > b: a, b = b, a
    x = b // a
    if b % a == 0:
        return a * (2 * x - 1)
    else:
        return a * 2 * x + reflect(b % a, a)

n, x = map(int,input().split())
print(reflect(x, n - x) + n)