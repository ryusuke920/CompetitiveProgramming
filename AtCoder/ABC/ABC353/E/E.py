def main() -> None:
    N = int(input())
    S = list(input().split())
    S.sort()
    pp = [len(S[i]) for i in range(N)]

    l = []
    l.append([-1]*26) # アルファベット
    num = [0]
    for i in range(N):
        s = S[i]
        x = 0
        for j in range(pp[i]):
            p = ord(s[j]) - ord("a")
            if l[x][p] == -1:
                l[x][p] = len(l)
                # print(i, j, p, l[x][p])
                l.append([-1]*26)
                num.append(0)
            x = l[x][p]
            num[x] += 1 # 同じ場合

    ans = 0
    # print(sum(num))
    for i in num:
        ans += i * (i - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()