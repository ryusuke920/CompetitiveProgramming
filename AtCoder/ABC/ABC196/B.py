x = input()
num = ""
for i in range(len(x)):
    if x[i] == ".":
        break
    num += x[i]
print(num)