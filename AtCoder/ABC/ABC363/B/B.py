'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc363/tasks/abc363_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc363/tasks/abc363_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, T, P = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 0
    while True:
        cnt = 0
        for i in range(N):
            if L[i] >= T:
                cnt += 1
        if cnt >= P:
            exit(print(ans))
        ans += 1
        for i in range(N):
            L[i] += 1

if __name__ == "__main__":
    main()