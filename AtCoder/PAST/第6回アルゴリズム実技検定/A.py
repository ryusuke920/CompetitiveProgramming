s = input()
number = "0123456789"
for i, j in enumerate(s):
    if i != 3:
        if j not in number:
            exit(print("No"))
    else:
        if j != "-":
            exit(print("No"))

print("Yes")