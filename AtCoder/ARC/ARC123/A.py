x, y, z = map(int,input().split())
num = 2 * y - x - z
if num == 0:
    print(0)
elif num < 0:
    if num % 2 == 0:
        print(-num // 2)
    elif num % 2 == 1:
        print(-(num - 1) // 2 + 1)
elif num > 0:
    print(num)