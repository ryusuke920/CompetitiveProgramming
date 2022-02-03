n = int(input())
cnt = 1
ans = 1
num = [cnt]
while ans < n:
    cnt += 1
    ans += cnt
    num.append(cnt)
if sum(num) == n:
    print(*num, sep = "\n")
else:
    ch = sum(num)-n
    for i in range(len(num)):
        if i == ch-1: continue
        else:
            print(num[i])