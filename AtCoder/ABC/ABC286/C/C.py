def main() -> None:
    n, a, b = map(int, input().split())
    s = list(input())
    ans = 10**18
    for i in range(1, n + 1):
        s = s[1:] + [s[0]]
        cost = a * (i % n)
        for j in range(n // 2):
            if s[j] != s[-1 - j]:
                cost += b
        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()