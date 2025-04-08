import sys
input = sys.stdin.readline

def main() -> None:
    A = int(input())
    if 400 % A:
        print(-1)
    else:
        print(400 // A)


if __name__ == "__main__":
    main()