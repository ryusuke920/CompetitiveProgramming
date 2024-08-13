'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc346/tasks/abc346_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc346/tasks/abc346_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def main() -> None:
    h, w, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)][::-1]
    d = defaultdict(int)
    for i in range(2*(10**5)+1):
        d[i] = 0
    d[0] = h*w

    sx, sy = set(), set()
    for i in range(m):
        t, a, c = l[i]
        if t == 1: # 横
            if not (1 <= a <= h):
                continue
            if a in sx:
                continue
            sx.add(a)
            d[c] += w - len(sy)
        if t == 2: # 縦
            if not (1 <= a <= w):
                continue
            if a in sy:
                continue
            sy.add(a)
            d[c] += h - len(sx)
    
    p = []
    cnt = 0
    for k, v in d.items():
        if v != 0 and k != 0:
            cnt += v

    d[0] = h*w - cnt
    for k, v in d.items():
        if v != 0:
            p.append((k, v))
    p.sort(key=lambda x: x[0])
    print(len(p))
    for i in p:
        print(i[0], i[1])

if __name__ == "__main__":
    main()