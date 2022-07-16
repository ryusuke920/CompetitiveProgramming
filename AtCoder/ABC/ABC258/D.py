def main() -> None:
    n, x = map(int, input().split())

    ans = float('inf')
    cost = 0
    for i in range(n):

        if x - i <= 0:
            break

        a, b = map(int, input().split())

        cnt = cost + a + b * (x - i)
        ans = min(ans, cnt)
        cost += a + b
    
    print(ans)

if __name__ == '__main__':
    main()