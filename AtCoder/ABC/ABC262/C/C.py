'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc262/tasks/abc262_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc262/tasks/abc262_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    cnt = 0
    for i in range(n):
        if a[i] == i + 1:
            cnt += 1
        else:
            if i + 1 ==  a[a[i] - 1]:
                ans += 1

    print(ans // 2 + cnt * (cnt - 1) // 2)


if __name__ == "__main__":
    main()