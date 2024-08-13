'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc346/tasks/abc346_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc346/tasks/abc346_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = k * (k + 1) // 2
    s = set()
    for i in range(n):
        if 1 <= a[i] <= k:
            s.add(a[i])
    cnt = 0
    for i in s:
        cnt += i
    print(ans - cnt)

if __name__ == "__main__":
    main()