from bisect import bisect_left, bisect_right

def LessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return bisect_left(A, K), (-1 if bisect_left(A, K) == 0 else bisect_left(A, K) - 1)

def More(K: int, A: list) -> int:
    "配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return len(A) - bisect_right(A, K), (bisect_right(A, K) if bisect_right(A, K) <= len(A) - 1 else -1)

def OrMore(K: int, A: list) -> int:
    "配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return len(A) - bisect_left(A, K), (bisect_left(A, K) if bisect_left(A, K) <= len(A) - 1 else -1)

def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return bisect_right(A, K), (-1 if bisect_right(A, K) == 0 else bisect_right(A, K) - 1)

"""
-d <= Xi - c <= d
c - d <= Xi <= c + d
Xi >= cのとき Xi - c 円 (1)
Xi < cのとき -(Xi - c) 円 (2)
Xi < c - dのとき d 円 (3)
Xi > c + dのとき d 円 (4)
"""
n, q = map(int,input().split())
x = list(map(int,input().split()))

wa = [x[0]]
for i in range(n - 1):
    wa.append(wa[-1] + x[i + 1])

print("x =", x)
print("wa =", wa)

for i in range(q):
    c, d = map(int,input().split())
    ans = 0
    i1, i2, i3 = LessThan(c - d, x), OrMore(c, x), More(c + d, x)
   # print(i1,i2,i3)
    ans += i1[0] * d
    ans += -((wa[i2[1]] - wa[max(i1[1], 0)]) - c * (i2[1] - max(i1[1], 0)))
    ans += ((wa[max(0, i3[1])] - wa[i2[1]]) - c * (max(0, i3[1]) - i2[1]))
    ans += (n - i3[1]) * d
    print(ans)