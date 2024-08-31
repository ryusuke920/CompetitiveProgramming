'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc369/tasks/abc369_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc369/tasks/abc369_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N - 1):
        B.append(A[i + 1] - A[i])
    INF = 10**18
    B.append(INF)    

    p = []
    ind = 1
    for i in range(N - 1):
        if B[i] == B[i + 1]:
            ind += 1
        else:
            p.append(ind)
            ind = 1
    
    ans = N
    print(p)
    for i in p:
        ans += i * (i + 1) // 2
    
    print(ans)
    

if __name__ == "__main__":
    main()