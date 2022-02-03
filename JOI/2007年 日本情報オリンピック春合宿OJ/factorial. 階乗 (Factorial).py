def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
n = int(input())
x = factorization(n)
ans = 0
for i in range(len(x)):
    ch = x[i][0]**x[i][1]
    if ans <= ch:
        ans = ch
        num = [x[i][0], x[i][1]]

i = 1
j = 2
count = 1
while num[1] > i:
    i += j
    j += 1
    count += 1
print(num[0]*count)