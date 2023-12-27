import sys
input = sys.stdin.readline

def add(i: int) -> None:
    global num, len_
    if num[i] == 0:
        len_ += 1
    num[i] += 1


def delete(i: int) -> None:
    global num, len_
    if num[i] == 1:
        len_ -= 1
    num[i] -= 1


n, q = map(int, input().split())
s = input()
block = int(n / q ** 0.5) + 1 # ブロックサイズ
queries = [[] for _ in range(int(q**0.5) + 1)] # クエリを受け取る配列

# クエリを受け取る
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    queries[l // block].append((i, l, r))

parity = 0 # 0 -> 通常
ans = [0] * q
left, right = 0, 0 # スタート地点は left, right ともに 0
num = [0] * (2*10**5 + 10) # num[i] := 今見ている区間 [left, right] に存在する i の個数
len_ = 0 # num に入っている要素数

for ind, query in enumerate(queries): # ソートしたクエリを1つずつ見ていく
    for i, l, r in sorted(query, reverse=ind%2, key=lambda x: x[2]): # ind(見ている縦のブロックが偶数のときは降順、奇数の時は昇順に並び替える)
        while right <= r:
            add(s[right])
            right += 1
        while l < left:
            left -= 1
            add(s[left])
        while r + 1 < right:
            right -= 1
            delete(s[right])
        while left < l:
            delete(s[left])
            left += 1

        ans[i] = len_ # num の中に入っている要素数を格納する

print(*ans, sep='\n')