a = [int(input()) for i in range(5)]
ans = 10
ch = {}
b = {}
num = 0
for i in range(5):
    b[i] = a[i]
    while True:
        a[i] = a[i]%10
        if a[i] == 0:
            a[i] = 10
        if a[i] <= 10:
            ch[i] = a[i]
            break
    ans = min(ch[i],ans)
for i in range(5):
    #print("b[",i,"]=",b[i])
    if b[i] <= 99:
        if b[i] %10 == 0:
            ans -= 10
        num += b[i] - b[i]%10
        #print("num",num)
    else:
        if b[i] %10 == 0:
            ans -= 10
        num += b[i] - (b[i] - 100)%10
print(ans + num + 40)