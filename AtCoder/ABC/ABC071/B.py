s = str(input())
s = sorted(set(s))
ch = "abcdefghijklnopqrstuvwxyz"
for i in ch:
    if i not in s:
        print(i)
        break
else:
    print("None")