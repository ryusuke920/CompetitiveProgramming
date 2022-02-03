import sys
from itertools import accumulate
N, C = map(int, input().split())
service = [None] * N
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1; b -= 1
    service[i] = (a, b + 1, c)  # imos法を見据えて, b は b + 1 とする

# 座標圧縮
day = set()
for a, b, c in service:
    day.add(a)
    day.add(b)

day = sorted(day)  # day[i]: 実日付を昇順に並べたリスト

D = {}  # D[d]: 実日付-->dayのインデックスに対応づけるためのマップ
for i, d in enumerate(day):
    D[d] = i
L = len(day)  # L: dayの長さ

# imos法
service.sort()
S = [0] * L
for a, b, c in service:
    S[D[a]] += c
    S[D[b]] -= c
T = list(accumulate(S)) # T[i]: 期間i(day[i + 1] - day[i])における1日あたりの従量料金

# 各期間iについて, 従量料金と定額料金を比較しどちらを採用するか決める。
# 期間の長さ(=日数)は day[i + 1] - day[i] により計算できる。

ans = 0
for i in range(L - 1):
    cost = min(T[i], C)
    days = day[i + 1] - day[i]
    ans += cost * days
print(ans)