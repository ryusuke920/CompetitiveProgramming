'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc369/tasks/abc369_g
oj t -c "python3 G.py"
oj s https://atcoder.jp/contests/abc369/tasks/abc369_g G.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    l, r = [], []
    for i in range(N):
        s, t = input().split()
        if t == "L":
            l.append(int(s))
        else:
            r.append(int(s))
    # l.sort()
    # r.sort()
    ans = 0
    for i in range(len(l) - 1):
        ans += abs(l[i + 1] - l[i])
    for i in range(len(r) - 1):
        ans += abs(r[i + 1] - r[i])
    print(ans)

if __name__ == "__main__":
    main()