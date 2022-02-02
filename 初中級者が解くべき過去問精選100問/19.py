from bisect import bisect_right
d = int(input()) # 全長
n = int(input()) # 店舗の個数
m = int(input()) # 注文の個数
shop = [0]
home = []
ans = 0
for i in range(n-1):
    shop.append(int(input()))
for i in range(m):
    home.append(int(input()))
shop.append(d) # 本店は１直線上では0とdは同値
shop.sort()

for i in home:
    x = bisect_right(shop, i)
    ans += min(abs(shop[x-1] - i), abs(shop[x] - i))
print(ans)