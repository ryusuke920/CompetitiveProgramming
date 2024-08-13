'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc347/tasks/abc347_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc347/tasks/abc347_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, a, b = map(int, input().split())
    d = list(map(int, input().split()))
    p = []
    for i in range(n):
        p.append(d[i] % (a + b))
    p.sort()
    # print(p)
    x = 0
    for i in range(n):
        l = p[i]
        r = p[(i + 1) % n]
        x = max(x, r - l - 1)
        
        if i == n - 1:
            x = max(x, (r + (a + b)) - 1 - l)
    
    if x < b:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()