n = int(input())
n = n%30
a = [1,2,3,4,5,6]
tmp = 0
for i in range(n):
    if i == 0:
        tmp = a[0]
        a[0] = a[1]
        a[1] = tmp
    elif i%5 != 0:
        tmp = a[i%5]
        a[i%5] = a[i%5+1]
        a[i%5+1] = tmp
    else:
        tmp = a[i%5]
        a[i%5] = a[i%5-5]
        a[i%5-5] = tmp
print(*a, sep = "")