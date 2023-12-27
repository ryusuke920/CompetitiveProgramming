'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc331/tasks/abc331_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc331/tasks/abc331_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, s, m, l = map(int, input().split())
    ans = 10**18

    for x in range(100):
        for y in range(100):
            for z in range(100):
                if x * 6 + y * 8 + z * 12 >= n:
                    ans = min(ans, s * x + m * y + l * z)
        
    print(ans)


if __name__ == "__main__":
    main()