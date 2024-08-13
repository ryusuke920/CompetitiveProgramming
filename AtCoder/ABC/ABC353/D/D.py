'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc353/tasks/abc353_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc353/tasks/abc353_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]*(N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    
    ans = 0
    l = [0]*N
    for i in range(N):
        l[i] = len(str(A[i]))
    mod = 998244353
    for i in range(1, N):
        cnt = S[i]
        cnt *= 10**(l[i])
        # cnt *= 10**(l[i] + 1)
        cnt %= mod
        cnt += A[i]*i
        ans += cnt 
        ans %= mod
        # print(i, ans)
    
    print(ans)

if __name__ == "__main__":
    main()