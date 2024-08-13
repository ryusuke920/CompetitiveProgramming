'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc350/tasks/abc350_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc350/tasks/abc350_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, Q = map(int, input().split())
    T = list(map(int, input().split()))
    cnt = [True]*N
    for i in range(Q):
        if cnt[T[i] - 1]:
            cnt[T[i] - 1] = False
        else:
            cnt[T[i] - 1] = True
    
    ans = 0
    for i in range(N):
        ans += cnt[i]
    
    print(ans)



if __name__ == "__main__":
    main()