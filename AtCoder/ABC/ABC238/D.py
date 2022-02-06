for _ in range(int(input())):
    a, s = map(int, input().split())
    
    if a > s:
        print('No')
    else:
        if a & (s - a) == a:
            print('Yes')
        else:
            print('No')