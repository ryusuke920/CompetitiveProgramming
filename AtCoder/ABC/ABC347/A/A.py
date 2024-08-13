'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc347/tasks/abc347_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc347/tasks/abc347_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] % k == 0:
            ans.append(a[i] // k)
    
    print(*ans)

if __name__ == "__main__":
    main()