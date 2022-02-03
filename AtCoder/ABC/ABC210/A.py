#n = int(input())
n,a,x, y = map(int,input().split())

if n <= a:
    print(x * n)
else:
    print(x * a + y * (n - a))