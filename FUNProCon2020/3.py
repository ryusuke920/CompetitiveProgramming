#n = int(input())
x,y = map(int,input().split())
mod = 10 ** 9 + 7
for i in range(y):
    x *= 2
    x%= mod
print(x%mod)