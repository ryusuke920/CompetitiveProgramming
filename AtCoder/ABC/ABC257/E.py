import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    c = list(map(int, input().split()))

    digit = n // min(c)

    ans = []

    for i in range(digit):
        for j in reversed(range(9)):
            if (digit - (i + 1)) * min(c) + c[j] <= n:
                n -= c[j]
                ans.append(str(j + 1))
                break

    print("".join(ans))
    

if __name__ == '__main__':
    main()