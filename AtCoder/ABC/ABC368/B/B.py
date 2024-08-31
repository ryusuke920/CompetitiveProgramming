'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc368/tasks/abc368_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc368/tasks/abc368_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        s = 0
        for i in A:
            if i >= 1:
                s += 1
        if s <= 1:
            break
        ans += 1
        A.sort(reverse=True)
        A[0] -= 1
        A[1] -= 1
        # print(ans, A)
    print(ans)

if __name__ == "__main__":
    main()