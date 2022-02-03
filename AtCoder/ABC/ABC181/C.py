n = int(input())
x = [0]*n
y = [0]*n

for i in range(n):
    x[i],y[i] = map(int,input().split())
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = [ [x[i],y[i]], [x[j],y[j]], [x[k],y[k]] ]
            a.sort()
            if ((a[1][1]-a[0][1])*(a[2][0]-a[1][0]) == (a[2][1]-a[1][1])*(a[1][0]-a[0][0])):
                print("Yes")
                exit()
print("No")