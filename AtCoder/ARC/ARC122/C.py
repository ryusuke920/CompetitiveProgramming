n = int(input())
f = [1, 1]
while True:
    num = f[-1] + f[-2]
    if num > 10 ** 18:
        break
    f.append(num)
print(f)
print(len(f))
