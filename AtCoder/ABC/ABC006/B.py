a = [0,0,1]
for i in range(int(input())-1):
    a[2],a[1],a[0] = a[1],a[0],(a[2]+a[1]+a[0])%10007
print(a[1])