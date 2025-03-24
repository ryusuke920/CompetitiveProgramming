'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc394/tasks/abc394_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc394/tasks/abc394_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    N = int(input())
    a = []
    for i in range(N):
        S = input()
        a.append((S, len(S)))
    a.sort(key=lambda x: x[1], reverse=False)
    ans = ""
    for i in range(N):
        ans += a[i][0]
    print(ans)

if __name__ == "__main__":
    main()