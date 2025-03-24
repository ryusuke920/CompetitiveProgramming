'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc398/tasks/abc398_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc398/tasks/abc398_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def check(x: int, y: int) -> bool:
    if A.count(x) >= 3 and A.count(y) >= 2:
        return True
    if A.count(x) >= 2 and A.count(y) >= 3:
        return True
    return False

def main() -> None:
    global A
    A = list(map(int, input().split()))
    for i in range(1, 14):
        for j in range(1, 14):
            if i == j:
                continue
            if check(i, j):
                exit(print("Yes"))
    print("No")


if __name__ == "__main__":
    main()