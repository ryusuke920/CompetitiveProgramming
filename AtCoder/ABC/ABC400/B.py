import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    X = 0
    for i in range(M + 1):
        X += N**i
        if X > 10**9:
            exit(print("inf"))
    print(X)


if __name__ == "__main__":
    main()