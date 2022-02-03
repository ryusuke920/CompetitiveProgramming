n = int(input())
for k in range(1, 31):
    num = 1
    for _ in range(k):
        num *= 3
    num += 1
    for _ in range(30 - k):
        num *= 3
    
    if num == n:
        exit(print(k))

print(-1)