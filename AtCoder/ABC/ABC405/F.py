from bisect import bisect_left, bisect_right
def bit_add(bit: int, i: int, v: int) -> None:
    n = len(bit)
    while i < n:
        bit[i] += v
        i += i & -i

def bit_sum(bit: int, i: int) -> int:
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
C = [0]*Q
D = [0]*Q
for i in range(Q):
    C[i], D[i] = map(int, input().split())

all_ab = []
for i, j in AB:
    all_ab.append(i)
    all_ab.append(j)
all_ab.sort()
# print(all_ab)
num = sorted({i for _, i in AB})
bit = [0]*(len(num) + 1)

AB.sort(key=lambda x: x[0])
cnt = []
for j in range(Q):
    cnt.append((D[j] - 1, j, 1))
    cnt.append((C[j], j, -1))
cnt.sort(key=lambda x: x[0])
# print(*cnt)
CC = [bisect_right(num, C[j])   for j in range(Q)]
DD = [bisect_right(num, D[j] - 1) for j in range(Q)]

p = [0]*Q
ind_ = 0
for t, i, sg in cnt:
    while ind_ < M and AB[ind_][0] <= t:
        a, b = AB[ind_]
        bi = bisect_left(num, b) + 1
        # print(a, b, bi)
        bit_add(bit, bi, 1)
        ind_ += 1
    p[i] += sg*(bit_sum(bit, DD[i]) - bit_sum(bit, CC[i]))

ans = []
for i in range(Q):
    t1 = bisect_left(all_ab, D[i])
    t2 = bisect_right(all_ab, C[i])
    # print(t1, t2)
    ans.append(t1 - t2 - 2*p[i])

print(*ans, sep="\n")