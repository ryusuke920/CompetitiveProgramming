n = int(input())
cnt = 0
for i in range(n):
    if input() == "black": cnt += 1
print("black") if cnt >= n // 2 + 1 else print("white")