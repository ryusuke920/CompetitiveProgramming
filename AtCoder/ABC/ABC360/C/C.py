'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc360/tasks/abc360_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc360/tasks/abc360_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    W = list(map(int, input().split()))
    num = [0]*N

    cnt = [[] for _ in range(N)]
    for i in range(N):
        cnt[A[i] - 1].append(W[i])
        num[A[i] - 1] += 1
    for i in range(N):
        cnt[i].sort()
    
    ans = 0
    for i in range(N):
        for j in range(num[i] - 1):
            ans += cnt[i][j]
    
    print(ans)


if __name__ == "__main__":
    main()