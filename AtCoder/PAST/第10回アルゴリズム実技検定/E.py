y, m, d = input().split('/')
print(y, m, d)

num = int(y)
while True:
    if len(set(str(num))) <= 2:
        break
    num += 1

y = num
print(y, m, d)