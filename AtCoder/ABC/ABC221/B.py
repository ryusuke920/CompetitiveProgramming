s = input()
t = list(input())

if list(s) == t:
    exit(print("Yes"))


for i in range(len(s) - 1):
    u = [i for i in s]
    u[i], u[i + 1] = u[i + 1], u[i]

    if u == t:
        exit(print("Yes"))

print("No")