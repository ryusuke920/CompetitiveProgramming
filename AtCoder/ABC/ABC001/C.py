from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
n,m = map(int,input().split())
n /= 10
m = float(m)
m /= 60
m += 0.01
m = round(m, 1)

# 風向
if 11.25 <= n and n < 33.75:
    d = "NNE"
elif 33.75 <= n and n < 56.25:
    d = "NE"
elif 56.25 <= n and n < 78.75:
    d = "ENE"
elif 78.75 <= n and n < 101.25:
    d = "E"
elif 101.25 <= n and n < 123.75:
    d = "ESE"
elif 123.75 <= n and n < 146.25:
    d = "SE"
elif 146.25 <= n and n < 168.75:
    d = "SSE"
elif 168.75 <= n and n < 191.25:
    d = "S"
elif 191.25 <= n and n < 213.75:
    d = "SSW"
elif 213.75 <= n and n < 236.25:
    d = "SW"
elif 236.25 <= n and n < 258.75:
    d = "WSW"
elif 258.75 <= n and n < 281.25:
    d = "W"
elif 281.25 <= n and n < 303.75: 
    d = "WNW"
elif 303.75 <= n and n < 326.25:
    d = "NW"
elif 326.25 <= n and n < 348.75:
    d = "NNW"
else:
    d = "N"

# 風速
if 0.0 <= m and m <= 0.2:
    s = 0
elif 0.3 <= m and m <= 1.5:
    s = 1
elif 1.6 <= m and m <= 3.3:
    s = 2
elif 3.4 <= m and m <= 5.4:
    s = 3
elif 5.5 <= m and m <= 7.9:
    s = 4
elif 8.0 <= m and m <= 10.7:
    s = 5
elif 10.8 <= m and m <= 13.8:
    s = 6
elif 13.9 <= m and m <= 17.1:
    s = 7
elif 17.2 <= m and m <= 20.7:
    s = 8
elif 20.8 <= m and m <= 24.4:
    s = 9
elif 24.5 <= m and m <= 28.4:
    s = 10
elif 28.5 <= m and m <= 32.6:
    s = 11
elif 32.7 <= m:
    s = 12

if s == 0:
    print("C",0)
else:
    print(d,s)    