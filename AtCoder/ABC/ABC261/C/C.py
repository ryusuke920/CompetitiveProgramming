'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc261/tasks/abc261_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc261/tasks/abc261_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''
from collections import defaultdict



def main() -> None:
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        if d[s] == 0:
            print(s)
        else:
            print(s + '(' + str(d[s]) + ')')
        d[s] += 1


if __name__ == "__main__":
    main()