n = int(input())
num = [0] * 2401
mod = [1, 2, 3, 4,]
for i in range(n):
    s = input()
    x = int(s[:4])
    y = int(s[5:])
    if x % 10 == 1 or x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
        x = x - x % 10
    elif x % 10 == 6 or x % 10 == 7 or x % 10 == 8 or x % 10 == 9:
        x = x - x % 10 + 5
    if y % 10 == 1 or y % 10 == 2 or y % 10 == 3 or y % 10 == 4:
        y = y - y % 10 + 5
    elif y % 10 == 6 or y % 10 == 7 or y % 10 == 8 or y % 10 == 9:
        y = y - y % 10 + 10
    if str(y)[2 :] == "60":
        y = y - 60 + 100
    for j in range(x, y + 1):
        num[j] = 1
check = False
for i in range(len(num)):
    if not check and num[i] == 1:
        check = True
        before = "0" * (4 - len(str(i))) + str(i)
    elif check and num[i] == 0:
        after = str(i - 1)
        print(before + "-" + after)
        check = False
if check:
    print(before + "-2400")