'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc355/tasks/abc355_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc355/tasks/abc355_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

N = 10**5
prt = [0]*(N+1)
left = [-1] + [0]*N
right = [-1] + [0]*N
sz = [0] + [1]*N
key = [0]*(N+1)
val = [0]*(N+1)
rev = [0]*(N+1)

def update(i, l, r):
    #assert 1 <= i <= N
    sz[i] = 1 + sz[l] + sz[r]
    val[i] = key[i] + val[l] + val[r]

def swap(i):
    if i:
        left[i], right[i] = right[i], left[i]
        rev[i] ^= 1

def prop(i):
    swap(left[i])
    swap(right[i])
    rev[i] = 0
    return 1

def splay(i):
    #assert 1 <= i <= N
    x = prt[i]
    rev[i] and prop(i)

    li = left[i]; ri = right[i]
    while x and not left[x] != i != right[x]:
        y = prt[x]
        if not y or left[y] != x != right[y]:
            if rev[x] and prop(x):
                li, ri = ri, li
                swap(li); swap(ri)

            if left[x] == i:
                left[x] = ri
                prt[ri] = x
                update(x, ri, right[x])
                ri = x
            else:
                right[x] = li
                prt[li] = x
                update(x, left[x], li)
                li = x
            x = y
            break

        rev[y] and prop(y)
        if rev[x] and prop(x):
            li, ri = ri, li
            swap(li); swap(ri)

        z = prt[y]
        if left[y] == x:
            if left[x] == i:
                v = left[y] = right[x]
                prt[v] = y
                update(y, v, right[y])

                left[x] = ri; right[x] = y
                prt[ri] = x
                update(x, ri, y)

                prt[y] = ri = x
            else:
                left[y] = ri
                prt[ri] = y
                update(y, ri, right[y])

                right[x] = li
                prt[li] = x
                update(x, left[x], li)

                li = x; ri = y
        else:
            if right[x] == i:
                v = right[y] = left[x]
                prt[v] = y
                update(y, left[y], v)

                left[x] = y; right[x] = li
                prt[li] = x
                update(x, y, li)

                prt[y] = li = x
            else:
                right[y] = li
                prt[li] = y
                update(y, left[y], li)

                left[x] = ri
                prt[ri] = x
                update(x, ri, right[x])

                li = y; ri = x

        x = z
        if left[z] == y:
            left[z] = i
            update(z, i, right[z])
        elif right[z] == y:
            right[z] = i
            update(z, left[z], i)
        else:
            break

    update(i, li, ri)
    left[i] = li; right[i] = ri
    prt[li] = prt[ri] = i
    prt[i] = x

    rev[i] = prt[0] = 0

def expose(i):
    p = 0
    cur = i
    while cur:
        splay(cur)
        right[cur] = p
        update(cur, left[cur], p)
        p = cur
        cur = prt[cur]
    splay(i)
    return p

def cut(i):
    expose(i)
    p = left[i]
    left[i] = prt[p] = 0
    return p

def link(i, p):
    expose(i)
    expose(p)
    prt[i] = p
    right[p] = i

def evert(i):
    expose(i)
    swap(i)
    rev[i] and prop(i)

def root(u):
    expose(u)
    while left[u]:
        u = left[u]
    splay(u)
    return u
 
def lca(u, v):
    expose(u)
    while left[u]:
        u = left[u]
    w = expose(v)
    while left[v]:
        v = left[v]
    return w if u == v else None


def main() -> None:
    N, L, R = map(int, input().split())
    INF = 10**18
    mod = 100
    # L -= 1
    # R -= 1
    R += 1 # [L, R)
    d, l = defaultdict(lambda: INF), {}
    l[L] = -1
    d[L] = 0
    q = deque([L])
    while q:
        v = q.popleft()
        if v == R: break
        if v == 0:
            question = N
        else:
            question = 0
            t = v
            # while t % 2:
            #     t //= 2
            #     question += 1
            while t % 2 == 0:
                t //= 2
                question += 1

        for i in range(question + 1):
            nxt = (1 << i) + v
            # v + (1 << i) <= R
            if nxt <= R and d[nxt] == INF:
                l[nxt] = v
                d[nxt] = d[v] + 1
                q.append(nxt)
            nxt = v - (1 << i)
            if nxt >= 0 and d[nxt] == INF:
                l[nxt] = v
                d[nxt] = d[v] + 1
                q.append(nxt)
            nxt = (1 << i) + v
            if d[nxt] == INF:
                l[nxt] = v
                d[nxt] = d[v] + 1
                q.append(nxt)
    a = []
    while True:
        if R == -1:
            break
        a.append(R)
        R = l[R]
    a = a[::-1]


    ans = 0
    len_ = len(a)
    for i in range(len_ - 1):
        if abs(a[i] - a[i + 1]) == 0:
            question = N
        else:
            question = 0
            t = abs(a[i] - a[i + 1])
            while t % 2 == 0:
                t //= 2
                question += 1
        min_ = INF
        if a[i] < a[i + 1]:
            min_ = a[i]
        else:
            min_ = a[i + 1]
        print(f"? {question} {min_ // (1 << question)}", flush=True)
        answer = int(input())
        if a[i] > a[i + 1]:
            ans += mod - answer
            ans %= mod
        else:
            ans += answer
            ans %= mod

    print(f"! {ans}", flush=True)


if __name__ == "__main__":
    main()