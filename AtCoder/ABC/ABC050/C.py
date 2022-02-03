n = int(input())
a = list(map(int,input().split()))
a.sort()
mod = 10**9 + 7
if n%2 == 1:
    for i in range(n):
        if a[i] != (i+1)//2*2:
            print(0)
            exit()
else:
    for i in range(n):
        if a[i] != i//2*2+1:
            print(0)
            exit()
print(2**(n//2)%mod)