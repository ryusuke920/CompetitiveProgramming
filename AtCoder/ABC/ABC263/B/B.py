'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc263/tasks/abc263_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc263/tasks/abc263_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n - 1):
        p[i] -= 1

    ans, cnt = 0, n - 1
    while True:
        cnt = p[cnt - 1]
        ans += 1
        if cnt == 0:
            break
    print(ans)

if __name__ == "__main__":
    main()