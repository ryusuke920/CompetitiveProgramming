n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    while True:
        if a[i]%2 == 0:
            count += 1
            a[i] //= 2
        else:
            break
print(count)