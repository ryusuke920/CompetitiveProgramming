n = int(input())
if n == 1:
    print(1)
elif n <= 3:
    print(2)
elif n <= 7:
    print(4)
elif n <= 15:
    print(8)
elif n <= 31:
    print(16)
elif n <= 63:
    print(32)
else:
    print(64)