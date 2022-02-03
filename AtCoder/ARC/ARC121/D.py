"""
4つの整数
a1 <= a 2 <= a3 <= a4について考えるか。
(i)minについて、
x := min(a1 + a4, a2 + a3) >= min(a1 + a3, a2 + a4)
(ii)maxについて、
y := max(a1 + a4, a2 + a3) <= max(a1 + a3, a2 + a4)

スワップさせるよりも両端の方が最適かー
だったら端から見てけばいいのか？だ、そうだわ行けたわ証明完了
"""

def big_samll(k):

    if (n + k) % 2 != 0:
        return INF
    l = [0] * k + a
    l.sort()
    num = []
    for i in range((n + k) // 2):
        num.append(l[-1 - i] + l[i])
    return max(num) - min(num)

n = int(input())
a = sorted(list(map(int,input().split())))
ans = INF = 10 ** 18
for i in range(n):
    ans = min(ans, big_samll(i))
print(ans)