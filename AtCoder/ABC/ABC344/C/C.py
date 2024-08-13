'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc344/tasks/abc344_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc344/tasks/abc344_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    p = set()
    for i in range(n):
        for j in range(m):
            p.add(a[i] + b[j])
    for i in range(q):
        qi = x[i]
        is_ok = False
        for j in range(l):
            if qi - c[j] in p:
                is_ok = True
        if is_ok:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()