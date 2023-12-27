n = int(input())
cnt = 0
while n > 0:
    if n % 2 == 1:
        n -= 1
        n //= 2
    else:
        n //= 2

    cnt += 1

print(cnt)