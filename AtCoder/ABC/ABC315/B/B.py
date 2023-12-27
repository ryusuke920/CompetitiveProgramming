import sys
input = sys.stdin.readline

def main() -> None:
    m = int(input())
    d = list(map(int, input().split()))
    s = sum(d) // 2
    p, q = 1, 0
    for i in range(s):
        if d[p - 1] == q:
            p += 1
            q = 0
        q += 1
    if d[p - 1] == q:
        print(p + 1, 1)
    else:
        print(p, q + 1)

if __name__ == "__main__":
    main()