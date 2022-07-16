def main() -> None:
    INF = 10 ** 18
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    s = 1
    e = n ** 2
    t = 0
    for i in range(n):
        for j in range(n):
            if t % 2 == 0:
                grid[i][j] = s
                s += 1
            else:
                grid[i][j] = e
                e -= 1
            t += 1

    for i in range(n):
        print(*grid[i])


if __name__ == '__main__':
    main()