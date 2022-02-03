s = input()
num = [0] * 3
for i in s:
    if i == "a":
        num[0] += 1
    elif i == "b":
        num[1] += 1
    elif i == "c":
        num[2] += 1

if max(num) == num[0]:
    print("a")
elif max(num) == num[1]:
    print("b")
elif max(num) == num[2]:
    print("c")