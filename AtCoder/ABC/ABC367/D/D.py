'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc367/tasks/abc367_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc367/tasks/abc367_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from collections import defaultdict

def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    s = [0]*(N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
        s[i + 1] %= M
    
    d = defaultdict(int)
    for i in range(N):
        d[s[i]] += 1
    
    cnt = 0
    for k, v in d.items():
        cnt += v * (v - 1) // 2
    
    num = s[N]
    for i in range(N):
        d[s[i]] -= 1
        cnt += d[num % M]
        num += A[i]
    
    print(cnt)


if __name__ == "__main__":
    main()