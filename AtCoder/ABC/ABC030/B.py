n,m = map(int,input().split())
n %= 12
lon = m*6
sho = n*30 + 30*m/60
a = abs(lon - sho)
b = 360 - a
print(min(a,b))