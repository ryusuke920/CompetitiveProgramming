n = int(input())
a = list(map(int,input().split()))
ave = sum(a)//n
b = c = 0
for i in range(n):
    b += (a[i]-ave)**2
    c += (a[i] - ave - 1)**2
print(min(b,c))