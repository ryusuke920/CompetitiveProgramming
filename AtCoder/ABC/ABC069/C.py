n = int(input())
a = list(map(int,input().split()))
count2 = 0
count4 = 0
for i in range(n):
    #２の倍数だが４の倍数でない
    if a[i]%2 == 0 and a[i]%4 != 0:
        count2 += 1
    #４の倍数
    elif a[i]%4 == 0:
        count4 += 1

if count4 != 0:
    count4 = count4*2

if count2 >= 2:
    count4 += count2-1

if count4 >= n-1:
    print("Yes")
else:
    print("No")