n = int(input())
for a1 in range(1, 11):
    for a2 in range(1, 11):
        if a1 + a2 == n:
            exit(print(a1, a2))