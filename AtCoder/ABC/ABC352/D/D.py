'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc352/tasks/abc352_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc352/tasks/abc352_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append((P[i], i))
    A.sort()

    s = set()
    for i in range(K):
        s.add(A[i][1])
    
    print(s)
    ans = max(s) - min(s)
    for i in range(N - K):
        s.remove(A[i][1])
        s.add(A[i + K][1])
        ans = min(ans, max(s) - min(s))
    
    print(ans)


if __name__ == "__main__":
    main()