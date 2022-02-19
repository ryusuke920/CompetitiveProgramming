a, b = map(int, input().split())
if a == 0:
    print('NO')
elif b == 0:
    print(0)
elif b % a == 0:
    print(b // a)
else:
    print('NO')