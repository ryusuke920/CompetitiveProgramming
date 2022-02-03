n = int(input())
ans = 2025 - n
for i in range(1,10):
    for j in range(1,10):
        if i*j == ans:
            print(i,"x",j)