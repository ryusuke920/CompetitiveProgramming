def main() -> None:
    N = int(input())
    S = input()
    T = input()
    ans = 0
    for i in range(N):
        ans += S[i] != T[i]
    print(ans)


if __name__ == "__main__":
    main()