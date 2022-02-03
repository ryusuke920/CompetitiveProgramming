a, b, c = map(int,input().split())
for i in range(a, b + 1):
    if i % c == 0:
        exit(print(i))
print(-1)