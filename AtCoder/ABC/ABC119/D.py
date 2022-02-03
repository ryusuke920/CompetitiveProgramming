from bisect import bisect_left

import sys
input = sys.stdin.readline

a, b, q = map(int,input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]

def search(a: list, l: int, now: int) -> int:
    """ある地点 now から最短の距離, 座標を返す"""

    p = bisect_left(a, now)
    now1, now2, now3 = -1, -1, -1
    
    if p == 0:
        dist = abs(now - a[p]); now1 = a[p]
    elif 1 <= p <= l - 1:
        dist1 = abs(now - a[p - 1]); now2 = a[p - 1]
        dist2 = abs(now - a[p]); now3 = a[p]
    else:
        dist = abs(now - a[p - 1]); now1 = a[p - 1]
    
    if now1 == -1: return dist1, dist2, now2, now3
    else: return dist, dist, now1, now1

for _ in range(q):

    now = int(input())

    dist1_1, dist1_2, now1_1, now1_2 = search(s, a, now)
    dist2_1, dist2_2, now2_1, now2_2 = search(t, b, now)
    dist3_1, dist3_2, now3_1, now3_2 = search(t, b, now1_1)
    dist4_1, dist4_2, now4_1, now4_2 = search(t, b, now1_2)
    dist5_1, dist5_2, now5_1, now5_2 = search(s, a, now2_1)
    dist6_1, dist6_2, now6_1, now6_2 = search(s, a, now2_2)

    ans1 = dist1_1 + dist3_1
    ans2 = dist1_1 + dist3_2
    ans3 = dist1_2 + dist4_1
    ans4 = dist1_2 + dist4_2
    ans5 = dist2_1 + dist5_1
    ans6 = dist2_1 + dist5_2
    ans7 = dist2_2 + dist6_1
    ans8 = dist2_2 + dist6_2

    print(min(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8))