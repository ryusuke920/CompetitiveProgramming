import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(min(a), max(a)):
        if i not in a:
            exit(print(i))

if __name__ == "__main__":
    main()