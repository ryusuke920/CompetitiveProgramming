n = int(input())

ans = 'AGC'
if n >= 42:
    print(ans + '0' + str(n + 1))
elif n >= 10:
    print(ans + '0' + str(n))
else:
    print(ans + '00' + str(n))