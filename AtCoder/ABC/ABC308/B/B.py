'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc308/tasks/abc308_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc308/tasks/abc308_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from collections import defaultdict

def main() -> None:
    n, m = map(int, input().split())
    c = list(input().split())
    d = list(input().split())
    p = list(map(int, input().split()))

    s = set()
    for i in d:
        s.add(i)
    
    di = defaultdict(int)
    for i in range(m):
        di[d[i]] = p[i + 1]

    ans = 0
    for i in range(n):
        if c[i] not in s:
            ans += p[0]
        else:
            ans += di[c[i]]
    
    print(ans)
    

if __name__ == "__main__":
    main()