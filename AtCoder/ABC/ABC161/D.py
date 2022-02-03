k = int(input())
num = [i+1 for i in range(9)]
for i in range(k):
    x = num[i]
    if x%10 != 0:
        num.append(x*10 + x%10 - 1)
    num.append(x*10 + x%10)
    if x%10 != 9:
        num.append(x*10 + x%10 + 1)
print(num[k - 1])