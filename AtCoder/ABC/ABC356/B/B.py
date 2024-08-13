'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc356/tasks/abc356_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc356/tasks/abc356_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0]*M
    for i in range(N):
        for j in range(M):
            cnt[j] += X[i][j]
    
    for i in range(M):
        if not (cnt[i] >= A[i]):
            exit(print("No"))
    
    print("Yes")


if __name__ == "__main__":
    main()