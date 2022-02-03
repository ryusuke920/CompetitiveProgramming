ma, da = map(int,input().split())
mb, db = map(int,input().split())
date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ma == mb:
    print(db - da)
else:
    mid = max(0, mb - ma - 1)
    mid_cnt = 0
    for i in range(mid):
        mid_cnt += date[i + ma]
    print((date[ma - 1] - da) + mid_cnt + db)