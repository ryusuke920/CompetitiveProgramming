h = int(input())
i = 1
while True:
    if h < 2**i:
        print(2**i-1)
        break
    i += 1