'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc326/tasks/abc326_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc326/tasks/abc326_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def judge(p: int) -> bool:
    l = list(str(p))
    if int(l[0]) * int(l[1]) == int(l[2]):
        return True
    else:
        return False

def main() -> None:
    n = int(input())
    while True:
        if judge(n):
            exit(print(n))
        n += 1


if __name__ == "__main__":
    main()