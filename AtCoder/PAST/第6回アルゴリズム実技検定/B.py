s = input()
for i in range(len(s) // 4):
    if s[i * 4: i * 4 + 4] == "post":
        exit(print(i + 1))

print("none")