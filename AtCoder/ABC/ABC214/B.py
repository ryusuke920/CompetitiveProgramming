s, t = map(int, input().split())

cnt = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k <= s and i * j * k <= t:
                cnt += 1

print(cnt)