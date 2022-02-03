n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = {}
ans = 0
for i in range(n):
    ans = max(ans, sum(a[0:i+1]) + sum(b[i:]) )
#    print("i=",i)
#    print( "sum(a[0:i+1])",sum(a[0:i+1]) )
#    print( "sum(b[i:])",sum(b[i:]) )
#    print()
print(ans)