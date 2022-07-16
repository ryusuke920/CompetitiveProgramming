n = int(input())
m = 2 * n

t = m // 8
if m % 8 == 0:
    x = '4' * t
elif m % 8 == 2:
    x = '1' + '4' * t
elif m % 8 == 4:
    x = '2' + '4' * t
else:
    x = '3' + '4' * t

print(m)
print(x)