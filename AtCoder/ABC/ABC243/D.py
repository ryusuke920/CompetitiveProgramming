n, x = input().split()
s = input()

x = list(bin(int(x)))

for i in s:
    if i == 'U':
        x.pop()
    if i == 'L':
        x.append("0")
    if i == 'R':
        x.append("1")

print(int("".join(x), 2))