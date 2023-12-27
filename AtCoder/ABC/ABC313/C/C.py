'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc313/tasks/abc313_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc313/tasks/abc313_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    s = sum(a)
    check = [s // n for _ in range(n)]
    for i in range(s % n):
        check[i] += 1
    
    ans = 0
    for i in range(n):
        ans += abs(check[i] - a[i])
    print(ans // 2)


if __name__ == "__main__":
    main()