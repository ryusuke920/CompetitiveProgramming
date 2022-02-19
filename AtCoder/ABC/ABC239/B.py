x = int(input())

if -9 <= x <= 9:
    print(0)
elif x % 10 == 0:
    print(str(x)[:-1])
else:
    num = int(str(x)[:-1])
    if num < 0:
        print(num - 1)
    else:
        print(num)