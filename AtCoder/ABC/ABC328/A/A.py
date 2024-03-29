'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc328/tasks/abc328_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc328/tasks/abc328_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, x = map(int, input().split())
    ans = 0
    s = list(map(int, input().split()))
    for i in s:
        if i <= x:
            ans += i
        
    print(ans)

if __name__ == "__main__":
    main()