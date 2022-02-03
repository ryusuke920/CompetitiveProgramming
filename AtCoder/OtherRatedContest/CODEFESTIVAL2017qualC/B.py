n = int(input())
a = list(map(int,input().split()))
cnt = 1
for i in range(n):
    if a[i]%2 == 0:
        cnt *= 2
    else:
        cnt *= 1
print(3**n-cnt)