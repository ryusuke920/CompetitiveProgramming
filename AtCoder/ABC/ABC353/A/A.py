'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc353/tasks/abc353_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc353/tasks/abc353_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[0] < H[i]:
            exit(print(i + 1))
    
    print(-1)


if __name__ == "__main__":
    main()