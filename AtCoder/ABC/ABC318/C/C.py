'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc318/tasks/abc318_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc318/tasks/abc318_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, d, p = map(int, input().split())
    f = list(map(int, input().split()))
    f.sort(reverse=True)

    i = 0
    cnt = 0
    while True:
        if i * d >= n:
            break
        normal = sum(f[i * d : min(n, (i + 1) * d)])
        if normal > p:
            cnt += 1
        i += 1

    ans = 0
    f.sort()
    for i in range(n - d * cnt):
        ans += f[i]
    print(ans + cnt * p)


if __name__ == "__main__":
    main()