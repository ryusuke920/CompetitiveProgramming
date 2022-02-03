n = input()
n = n[::-1]
a = b = 0
for i in range(len(n)):
    if i%2 == 0:
        a += int(n[i])
    else:
        b += int(n[i])
print(b,a)