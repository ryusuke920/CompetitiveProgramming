a, b = input().split()
a = a[::-1]
b = b[::-1]
a = list(a)
b = list(b)
for i, j in zip(a, b):
    if int(i) + int(j) >= 10:
        exit(print("Hard"))

print("Easy")