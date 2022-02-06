a = [int(input()) for _ in range(5)]
pasta = min(a[0], a[1], a[2])
juice = min(a[3], a[4])
print(pasta + juice - 50)