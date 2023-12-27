'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc311/tasks/abc311_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc311/tasks/abc311_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n, d = map(int, input().split())
    s = [input() for _ in range(n)]

    ans = 0
    for start in range(n):
        for end in range(start, n):
            bool = True
            for i in range(n):
                for j in range(start, end + 1):
                    if s[i][j] == "x":
                        bool = False
            
            if bool:
                ans = max(ans, end - start + 1)



if __name__ == "__main__":
    main()