'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc263/tasks/abc263_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc263/tasks/abc263_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''
from itertools import permutations

n, m = map(int, input().split())
for i in permutations(range(m), n):
    l = [j + 1 for j in i]
    check = True
    for j in range(n - 1):
        if not (l[j] < l[j + 1]):
            check = False
            break
    if check:
        print(*l)