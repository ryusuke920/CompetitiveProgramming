a,b,k = map(int,input().split())
turn = 1
for i in range(k):
    if turn%2 == 1:
        if a%2 == 0:
            a //= 2
            b += a
        else: #a%2 == 1:
            a -= 1
            a //= 2
            b += a
    else: #turn == 2:
        if b%2 == 0:
            b //= 2
            a += b
        else: #a%2 == 1:
            b -= 1
            b //= 2
            a += b
    turn += 1
print(a,b)