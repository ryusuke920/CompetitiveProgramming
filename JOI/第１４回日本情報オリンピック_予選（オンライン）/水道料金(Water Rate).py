a = [int(input()) for _ in range(5)] # X社(円/L）、Yの基本料金、Yの使用上限、追加料金(円/L)、１ヶ月の使用上限
x = a[0] * a[4]
if a[2] >= a[4]:
    y = a[1]
else:
    y = a[1]
    y += (a[4] - a[2]) * a[3]
print(min(x, y))