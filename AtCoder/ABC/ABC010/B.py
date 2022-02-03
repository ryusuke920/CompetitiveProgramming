n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    if a[i] == 1 or a[i] == 3 or a[i] == 7 or a[i] == 9:
        count += 0
    elif a[i] == 2 or a[i] == 4 or a[i] == 8:
        count += 1
    elif a[i] == 5:
        count += 2
    else:
        count += 3
print(count)