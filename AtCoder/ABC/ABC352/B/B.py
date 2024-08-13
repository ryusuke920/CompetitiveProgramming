'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc352/tasks/abc352_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc352/tasks/abc352_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    S = input()
    T = input()
    l1 = len(S)
    l2 = len(T)
    now = 0
    ans = []
    for i in range(l2):
        if T[i] == S[now]:
            ans.append(i + 1)
            now += 1

    print(*ans)

if __name__ == "__main__":
    main()