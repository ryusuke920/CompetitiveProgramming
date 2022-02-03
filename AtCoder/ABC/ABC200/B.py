#n = int(input())
n,k = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
for i in range(k):
    if n % 200 == 0:
        n //= 200
    else:
        n = str(n)
        n += "200"
        n = int(n)
print(n)