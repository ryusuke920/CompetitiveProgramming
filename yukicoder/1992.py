n = int(input())

pattern = 'AABBABB'

now = 0
d = 0
i = 0
while True:
    c = pattern[i % 7]
    
    if c == 'A':
        now += 2
        d += 2
    elif c == 'B':
        now -= 1
        d += 1
    
    if now == n:
        print(d)
        exit()

    i += 1