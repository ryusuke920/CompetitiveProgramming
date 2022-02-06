n = int(input())
a, b, c = map(int, input().split())

if a == c:
    print('No')
else:
    if b < a < c or c < a < b:
        print('No')
    else:
        print('Yes')