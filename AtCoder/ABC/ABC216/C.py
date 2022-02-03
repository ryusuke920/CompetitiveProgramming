n = int(input())
num = n

ans = ''
while 1 < num:
    if num % 2 == 0:
        num //= 2
        ans += 'B'
    else:
        num -= 1
        ans += 'A'

print('A' + ans[::-1])