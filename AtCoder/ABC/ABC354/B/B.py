'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc354/tasks/abc354_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc354/tasks/abc354_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    N = int(input())
    S = []
    T = 0
    for i in range(N):
        s, c = input().split()
        c = int(c)
        S.append(s)
        T += c
    S.sort()
    print(S[T % N])


if __name__ == "__main__":
    main()