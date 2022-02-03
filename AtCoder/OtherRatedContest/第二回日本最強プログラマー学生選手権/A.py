x, y, z = map(int,input().split())
ans = cnt = 1
while True:
    if y * z <= ans * x:
        exit(print(ans - 1))
    ans += 1