n,m,a,b = map(int,input().split())
c = [int(input()) for _ in range(m)]
num = n
for i in range(m):
    if num <= a:
        num += b
    num -= c[i]
    if num < 0:
        print(i+1)
        exit()
print("complete")