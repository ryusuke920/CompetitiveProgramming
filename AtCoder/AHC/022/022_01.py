import sys
input = sys.stdin.readline

def deploy() -> None:
    for i in range(l):
        print(*p[i])
    sys.stdout.flush()

def measure() -> None:
    pass

def answer() -> None:
    print(-1, -1, -1)
    for i in range(n):
        print(ans[i])
    sys.stdout.flush()


def main() -> None:
    global l, n, s, y, x, p, ans

    l, n, s = map(int, input().split())
    y, x = [0] * n, [0] * n
    for i in range(n):
        y[i], x[i] = map(int, input().split())
    
    p = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            p[i][j] = (i * l + j) % 1000
    ans = [1] * n

    deploy()
    answer()

    


if __name__ == "__main__":
    main()