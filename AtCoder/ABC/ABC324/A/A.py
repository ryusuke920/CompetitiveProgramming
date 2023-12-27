import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()