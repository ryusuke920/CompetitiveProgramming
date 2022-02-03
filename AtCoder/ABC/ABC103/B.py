a = input()
b = input()
a *= 2
for i in a:
    if b in a:
        print("Yes")
        break
else:
    print("No")