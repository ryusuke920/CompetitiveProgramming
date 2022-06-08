from math import gcd


def f(n: int) -> int:
    return n * (n + 1) // 2


def g(n: int, a: int) -> int:
    return f(n // a) * a


def main() -> None:
    n, a, b = map(int, input().split())

    ans = f(n)
    ans -= g(n, a)
    ans -= g(n, b)
    ans += g(n, a * b // gcd(a, b))

    print(ans)


if __name__ == '__main__':
    main()