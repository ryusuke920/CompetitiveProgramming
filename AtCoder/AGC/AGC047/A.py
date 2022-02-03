n = int(input())
a = [float(input())*10**9 for _ in range(n)]
div = [0]*2*n #2,5の約数の個数を管理
num = a
for i in range(n):
    while True:
        if num[i]%2 != 0:
            break
        else:
            div[2*i] += 1
            num[i] //= 2
    while True:
        if num[i]%5 != 0:
            break
        else:
            div[2*i+1] += 1
            num[i] //= 5

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if div[2*i]+div[2*j] >= 18 and div[2*i+1]+div[2*j+1] >= 18:
            ans += 1
print(ans)