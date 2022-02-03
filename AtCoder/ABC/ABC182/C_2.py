n = int(input())
if n % 3 == 0:
    print(0)
else:
    s = 0
    for i in range(len(str(n))):
        s += int(str(n)[i])
    for i in range(len(str(n))):
        if (s - int(str(n)[i])) % 3 == 0 and len(str(n)) >= 2:
            exit(print(1))
    
    for i in range(len(str(n))):
        for j in range(len(str(n))):
            if i == j: continue
            if (s - int(str(n)[j]) - int(str(n)[j])) % 3 == 0 and len(str(n)) >= 3:
                exit(print(2))
    
    print(-1)