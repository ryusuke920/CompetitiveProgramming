'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc310/tasks/abc310_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc310/tasks/abc310_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import defaultdict

def main() -> None:
    N = int(input())
    S = [input() for _ in range(N)]
    s = set()
    for i in range(N):
        if S[i] not in s and S[i][::-1] not in s:
            s.add(S[i])
    print(len(s))


if __name__ == "__main__":
    main()