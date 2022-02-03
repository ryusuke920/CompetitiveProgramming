a = list(map(str,input().split()))
count = 0
for i in range(int(a[0]),int(a[1])+1):
    ch = str(i)
    if ch == ch[::-1]:
        count += 1
print(count)