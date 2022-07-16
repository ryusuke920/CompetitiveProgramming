def main() -> None:
    x, a, d, n = map(int, input().split())

    mi = a
    ma = a + d * (n - 1)

    if mi > ma:
        mi, ma = ma, mi

    if x <= mi:
        print(mi - x)
    elif x >= ma:
        print(x - ma)
    else:
        if d < 0:
            d *= -1

        ans = (x - a) % d
        print(min(ans, -ans % d))


if __name__ == '__main__':
    main()