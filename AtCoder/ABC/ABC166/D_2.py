x = int(input())
for i in range(-2000, 2001):
    for j in range(-2000, 2001):
        if i ** 5 - j ** 5 == x:
            exit(print(i, j))