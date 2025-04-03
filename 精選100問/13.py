from itertools import product
r,c = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
ans = 0
for bit in product([0,1], repeat = r):
    num = 0 # ある部分和に対する全体での０の数をカウント
    for i in range(c):
        cnt = 0 # 列ごとの０の数をカウント
        for j in range(r):
            if bit[j] == 0 and a[j][i] == 0:
                cnt += 1
            elif bit[j] == 1 and a[j][i] == 1:
                cnt += 1
        num += max(cnt, r-cnt)
    ans = max(ans, num)
print(ans)