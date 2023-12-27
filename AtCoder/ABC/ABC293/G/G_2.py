'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc293/tasks/abc293_g
oj t -c "python3 G.py"
oj s https://atcoder.jp/contests/abc293/tasks/abc293_g G.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def add(i: int) -> None:
    global cnt
    num[i] += 1
    cnt += num[i] * (num[i] - 1) * (num[i] - 2) // 6 - (num[i] - 1) * (num[i] - 2) * (num[i] - 3) // 6


def delete(i: int) -> None:
    global cnt
    cnt -= num[i] * (num[i] - 1) * (num[i] - 2) // 6 - (num[i] - 1) * (num[i] - 2) * (num[i] - 3) // 6
    num[i] -= 1

n, q = map(int, input().split())
a = list(map(int, input().split()))
block = int(n / q ** 0.5) + 1 # ブロックサイズ
queries = [[] for _ in range(int(q**0.5) + 1)] # クエリを受け取る配列

# クエリを受け取る
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    queries[l // block].append((i, l, r))

ans = [0] * q
left, right = 0, 0 # スタート地点は left, right ともに 0
num = [0] * (2*10**5 + 10) # num[i] := 今見ている区間 [left, right] に存在する i の個数
cnt = 0

for ind, query in enumerate(queries): # ソートしたクエリを1つずつ見ていく
    for i, l, r in sorted(query, reverse=ind%2, key=lambda x: x[2]): # ind(見ている縦のブロックが偶数のときは降順、奇数の時は昇順に並び替える)
        while right <= r:
            add(a[right])
            right += 1
        while l < left:
            left -= 1
            add(a[left])
        while r + 1 < right:
            right -= 1
            delete(a[right])
        while left < l:
            delete(a[left])
            left += 1
        ans[i] = cnt

print(*ans, sep='\n')