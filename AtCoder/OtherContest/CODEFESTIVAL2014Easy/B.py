n = int(input())
if n%40 == 0:
    print(1)
elif n%40 >= 21:
    print(41-n%40)
else:
    print(n%40)