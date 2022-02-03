l,x,y,s,d = map(int,input().split())
if s == d:
    exit(print(0))
elif s < d:
    dis1 = s + l - d # 反時計回り
    dis2 = d - s # 時計回り
    if x < y: # 床 < 高橋くん
        ans1 = dis1 / (y - x)
        ans2 = dis2 / (x + y)
        print(min(ans1, ans2))
    else:
        ans2 = dis2 / (x + y)
        print(ans2)
else:
    dis1 = s - d # 反時計回り
    dis2 = d + l - s # 時計回り
    if x < y: # 床 < 高橋くん
        ans1 = dis1 / (y - x)
        ans2 = dis2 / (x + y)
        print(min(ans1, ans2))
    else:
        ans2 = dis2 / (x + y)
        print(ans2)