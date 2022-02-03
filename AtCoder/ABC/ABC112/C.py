n = int(input())
xyh = []
for i in range(n):
    num = list(map(int,input().split()))
    xyh.append(num)
    if num[2] >= 1:
        tx, ty, th = num

# ピラミッドの高さを全探索
for cx in range(101):
    for cy in range(101):
        H = th + abs(cx - tx) + abs(cy - ty)
        if all(h == max(H - abs(x - cx) - abs(y - cy), 0) for x, y, h in xyh):
            exit(print(cx, cy, H))