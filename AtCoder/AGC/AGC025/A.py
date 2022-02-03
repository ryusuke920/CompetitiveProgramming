n = int(input())
if n%10 == 0:
    print(10)
else:
    cnt = 0
    while n != 0:
        cnt += n%10
        n //= 10
    print(cnt)