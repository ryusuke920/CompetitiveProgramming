"""
全てのワームホールから動かず探索し計測値の高い順に答えを出す
"""

import sys
input = sys.stdin.readline


def deploy() -> None:
    for i in range(l):
        print(*p[i], flush=True)


def measure() -> None:
    measure_score = [[0, 0] for _ in range(n)]
    for i in range(n):
        print(i, 0, 0, flush=True)
        measure_score[i] = [i, int(input())]
    measure_score.sort(key= lambda x: x[1], reverse=True)

    for i in range(n):
        ans[n - i - 1] = measure_score[i][0]


def answer() -> None:
    print(-1, -1, -1, flush=True)
    for i in range(n):
        print(ans[i], flush=True)


def main() -> None:
    global l, n, s, y, x, p, ans

    l, n, s = map(int, input().split())
    y, x = [0] * n, [0] * n
    for i in range(n):
        y[i], x[i] = map(int, input().split())

    p = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            p[i][j] = (i * l + j) // 3

    ans = [0] * n
    deploy()
    measure()
    answer()


if __name__ == "__main__":
    main()