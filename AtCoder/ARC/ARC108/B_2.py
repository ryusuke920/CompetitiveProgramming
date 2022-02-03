n = int(input())
s = input()
fox = ""
l = 0
cnt = 0
for i in s:
    if i in "fox":
        fox += i
        l += 1
    else:
        fox = ""
        l = 0
    if l >= 3:
        if fox[-3] + fox[-2] + fox[-1] == "fox":
            cnt += 1
            fox = fox[:l - 3]
            l -= 3
print(n - cnt * 3)