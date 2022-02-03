s = input()
num = "0123456789"
for i in range(3):
    if s[i] not in num:
        exit(print("error"))
print(int(s) * 2)