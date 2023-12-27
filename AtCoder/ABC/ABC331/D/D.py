def get_sum(x1, y1, x2, y2) -> int:
    return sum_[x2][y2] - sum_[x1][y2] - sum_[x2][y1] + sum_[x1][y1]

def main() -> None:
    n, query = map(int, input().split())
    p = [input() for _ in range(n)]
    a, b, c, d = [], [], [], []
    for _ in range(query):
        pp, q, r, s = map(int, input().split())
        a.append(pp)
        b.append(q)
        c.append(r)
        d.append(s)
    global sum_
    sum_ = [[0] * 1001 for _ in range(1001)]

    for i in range(n):
        for j in range(n):
            sum_[i + 1][j + 1] = sum_[i][j + 1] + sum_[i + 1][j] - sum_[i][j] + (p[i][j] == 'b')

    for i in range(query):
        c[i] += 1
        d[i] += 1
        x = a[i] // n
        a[i] -= x * n
        c[i] -= x * n
        y = b[i] // n
        b[i] -= y * n
        d[i] -= y * n

        ans = 0

        if b[i] != 0 and a[i] != 0:
            ans += get_sum(a[i], b[i], n, n)

        if b[i] != 0:
            ans += get_sum(0, b[i], c[i] % n, n)

        w = ((d[i] - b[i]) - (n - b[i]) % n - (d[i]) % n) // n
        if a[i] != 0:
            ans += get_sum(a[i], 0, n, n) * w

        ans += get_sum(0, 0, c[i] % n, n) * w

        if a[i] != 0:
            ans += get_sum(a[i], 0, n, d[i] % n)

        ans += get_sum(0, 0, c[i] % n, d[i] % n)

        h = ((c[i] - a[i]) - (n - a[i]) % n - c[i] % n) // n
        if b[i] != 0:
            ans += get_sum(0, b[i], n, n) * h

        ans += get_sum(0, 0, n, d[i] % n) * h
        ans += sum_[n][n] * h * w
        print(ans)


if __name__ == "__main__":
    main()