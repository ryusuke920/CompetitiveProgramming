for _ in range(int(input())):
    p, q = map(int, input().split())
    a, b, c = map(int, input().split())
    s = set()
    while True:
        check = [0, 0]
        p = (a * p + b) % c
        q = (a * q + b) % c
        
        if p in s:
            check[0] = 1

        if q in s:
            check[1] = 1
        
        if check[0] == 0:
            s.add(p)
        if check[1] == 0:
            s.add(q)
        
        if check == [1, 1]:
            print('Draw')
            break
        elif check == [0, 1]:
            print('Acom')
            break
        elif check == [1, 0]:
            print('Pany')
            break