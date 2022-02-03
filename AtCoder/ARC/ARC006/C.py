n = int(input())
w = [int(input()) for _ in range(n)]
num = []
num.append(w[0])
for i in range(n - 1):
    cnt = 10 ** 9
    for j in range(len(num)):
        if 0 <= num[j] - w[i + 1] < cnt:
            cnt = num[j] - w[i + 1]
    if cnt == 10 ** 9:
        num.append(w[i + 1])
    else:
        for j in range(len(num)):
            if num[j] - w[i + 1] == cnt:
                num[j] = w[i + 1]
                break
print(len(num))