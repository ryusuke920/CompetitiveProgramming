x1, y1, x2, y2 = map(int, input().split())
for a in range(x1 - 100, x1 + 100):
    for b in range(y1 - 100, y1 + 100):
        dist_1 = ((x1 - a) ** 2 + (y1 - b) ** 2)
        dist_2 = ((x2 - a) ** 2 + (y2 - b) ** 2)

        if dist_1 == 5 and dist_2 == 5:
            exit(print('Yes'))

print('No')