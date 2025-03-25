'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc393/tasks/abc393_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc393/tasks/abc393_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from collections import defaultdict

def main() -> None:
    N, M = map(int, input().split())
    d = defaultdict(int)
    ans = 0
    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        if u == v:
            ans += 1
        else:
            u, v = min(u, v), max(u, v)
            if d[f"{u}-{v}"] != 0:
                ans += 1
            else:
                d[f"{u}-{v}"] += 1
    
    print(ans)


if __name__ == "__main__":
    main()