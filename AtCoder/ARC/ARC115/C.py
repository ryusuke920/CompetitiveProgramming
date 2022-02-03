n = int(input())
num = []
i = cnt = 1
nt = i * 2
while True:
    while i < nt:
        num.append(cnt)
        i += 1
    cnt += 1
    i = nt
    nt = i * 2
    if i > n:
        break
num = num[:n]
print(*num)