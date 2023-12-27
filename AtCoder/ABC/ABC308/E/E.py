'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc308/tasks/abc308_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc308/tasks/abc308_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    m, x = [[0] * (n + 1) for _ in range(3)], [[0] * (n + 1) for _ in range(3)]

    for i in range(n):
        if s[i] == "M":
            m[a[i]][i + 1] += 1
        elif s[i] == "X":
            x[a[i]][i + 1] += 1
    #print(*m, sep="\n")
    for i in range(3):
        for j in range(n):
            m[i][j + 1] += m[i][j]
            x[i][j + 1] += x[i][j]
    
    ans = 0
    for i in range(n):
        if s[i] == "E":
            for l in range(3):
                for r in range(3):
                    p = [a[i], l, r]
                    p.sort()
                    cnt = 0
                    for t in p:
                        if t == cnt:
                            cnt += 1
                    ans += cnt * (m[l][i] - m[l][0]) * (x[r][n] - x[r][i + 1])
                    #print(ans, cnt, m[l][i] - m[l][0], x[r][n] - x[r][i + 1])
    
    print(ans)


if __name__ == "__main__":
    main()