n = int(input())
a = [int(input()) for _ in range(n)]
ans = [0]*n
count = 0
num = a[0]
index = 1
while ans[1] != 1:
    count += 1
    ans[index-1] += 1
    if ans[index-1] >= 2:
        print(-1)
        exit()
    index = num
    num = a[num-1]
print(count-1)