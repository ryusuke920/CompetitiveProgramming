N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        if 4 * h * n - N * n - N * h != 0:
            w = N * h * n // (4 * h * n - N * n - N * h)
            if 4 / N == 1 / h + 1 / n + 1 / w and w > 0:
                exit(print(h, n, w))