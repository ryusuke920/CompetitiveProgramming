n = int(input())
for i in range(1, 3501):
    for j in range(1, 3501):
        under = 4 * i * j - n * (i + j)
        if under <= 0: continue
        up = i * j * n 
        k = up // under
        if 4 / n == 1 / i + 1 / j + 1/ k:
                exit(print(i, j, int(k)))