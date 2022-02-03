n = int(input())
a = list(map(int,input().split()))
a = [0] + a + [0]
num = 0
for i in range(n+1):
    num += abs(a[i+1]-a[i])
for i in range(1,n+1):
    print( num - abs(a[i]-a[i-1]) - abs(a[i+1]-a[i]) + abs(a[i+1]-a[i-1]))