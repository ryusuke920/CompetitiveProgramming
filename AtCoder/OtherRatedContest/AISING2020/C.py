num = [0] * 40000
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            n = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            num[n - 1] += 1
a = int(input())
for i in range(a):
    print(num[i])