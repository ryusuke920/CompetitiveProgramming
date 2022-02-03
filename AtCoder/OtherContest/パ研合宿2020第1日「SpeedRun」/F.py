p = int(input())
num = [1, 1]
i = 0
while len(num) <= 50000:
    x = num[i] + num[i + 1]
    i += 1
    num.append(x)
for i in range(len(num)):
    if num[i] % p == 0:
        exit(print(i + 1))
print(-1)