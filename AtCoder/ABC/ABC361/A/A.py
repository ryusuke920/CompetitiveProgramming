'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc361/tasks/abc361_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc361/tasks/abc361_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = A[:K] + [X] + A[K:]
    print(*ans)


if __name__ == "__main__":
    main()