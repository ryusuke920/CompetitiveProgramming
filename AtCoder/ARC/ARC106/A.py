n = int(input())
for b in range(1,60):
    for a in range(1,200):
        if 3**a + 5**b == n:
            print(a,b)
            exit()
print(-1)