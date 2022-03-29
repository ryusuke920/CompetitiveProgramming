a, b, c, d = map(int, input().split())

if a > c:
    print('Aoki')
elif a < c:
    print('Takahashi')
elif a == c:
    if b == d:
        print('Takahashi')
    elif b > d:
        print('Aoki')
    elif b < d:
        print('Takahashi')