'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc311/tasks/abc311_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc311/tasks/abc311_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    
    x = []
    start = 0
    is_ok = set()
    while start not in is_ok:
        is_ok.add(start)
        start = a[start]
    cur = a[start]
    while cur != start:
        x.append(cur)
        cur = a[cur]
    x.append(cur)

    print(len(x))
    print(*[i + 1 for i in x])

if __name__ == "__main__":
    main()