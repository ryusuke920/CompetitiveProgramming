def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s, t = [], []
    for i in range(n - 1):
        p, q = map(int, input().split())
        s.append(p)
        t.append(q)
    
    for i in range(n - 1):
        a[i + 1] += a[i] // s[i] * t[i]
    
    print(a[n - 1])


if __name__ == "__main__":
    main()