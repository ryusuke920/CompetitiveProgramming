s = list(input())

x, y = 0, 0
l = len(s)

for i in range(l):
    if s[i] == 'a':
        x += 1
    else:
        break

for i in range(l - 1, -1, -1):
    if s[i] == 'a':
        y += 1
    else:
        break

if y >= x:
    word = ["a"] * (y - x) + s
    if word == word[::-1]:
        exit(print('Yes'))

print("No")