import sys
input = sys.stdin.readline

def main() -> None:
    n, h, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if h + p[i] >= x:
            exit(print(i + 1))


if __name__ == "__main__":
    main()