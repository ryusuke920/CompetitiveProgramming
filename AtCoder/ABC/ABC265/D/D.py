'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc265/tasks/abc265_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc265/tasks/abc265_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, p, q, R = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = [[] for _ in range(3)]
    l = 0
    num = 0
    for r in range(n):
        num += a[r]
        while num > p:
            if l > r:
                break
            num -= a[l]
            l += 1
        if num == p:
            cnt[0].append((l, r))
    l = 0
    num = 0
    for r in range(n):
        num += a[r]
        while num > q:
            if l > r:
                break
            num -= a[l]
            l += 1
        if num == q:
            cnt[1].append((l, r))
    l = 0
    num = 0
    for r in range(n):
        num += a[r]
        while num > R:
            if l > r:
                break
            num -= a[l]
            l += 1
        if num == R:
            cnt[2].append((l, r))
    #print(*cnt,sep='\n')
    from collections import defaultdict

    d1 = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    for i in range(3):
        for ii, jj in cnt[i]:
            if i == 0:
                d1[ii] = jj
            if i == 1:
                d2[ii] = jj
            if i == 2:
                d3[ii] = jj
    
    bool = False
    for ii, jj in cnt[0]:
        if d2[jj + 1] != 0:
        #print('koko', ii, jj, d2[jj + 1])
            num = d2[jj + 1]
            if d3[num + 1] != 0:
                bool = True
                break

    print('Yes') if bool else print('No')


if __name__ == "__main__":
    main()