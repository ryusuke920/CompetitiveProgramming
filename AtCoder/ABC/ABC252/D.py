from collections import defaultdict

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(int)
    for i in a:
        d[i] += 1

    ans = n * (n - 1) * (n - 2) // 6

    two, three = 0, 0
    for v in d.values():
        if v >= 2:
            two += (n - v) * (v * (v - 1) // 2)
        if v >= 3:
            three += v * (v - 1) * (v - 2) // 6

    print(ans - two - three)

if __name__ == '__main__':
    main()