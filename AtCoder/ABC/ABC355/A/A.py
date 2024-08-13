import sys
input = sys.stdin.readline

def main() -> None:
    A, B = map(int, input().split())
    if A == B:
        print(-1)
    else:
        print(6 - (A + B))


if __name__ == "__main__":
    main()