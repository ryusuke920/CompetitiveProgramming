'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc348/tasks/abc348_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc348/tasks/abc348_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def main() -> None:
    n = int(input())
    a, c = [0] * n, [0] * n
    INF = 10**18
    d = defaultdict(lambda : INF)
    for i in range(n):
        a[i], c[i] = map(int, input().split())
        d[c[i]] = min(d[c[i]], a[i])
    
    ans = []
    for k, v in d.items():
        ans.append(v)
    print(max(ans))
    print(ans)


if __name__ == "__main__":
    main()