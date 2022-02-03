from collections import Counter
s = input()
y = s[:4]
d = s[5:7]
m = s[8:10]
dm = d+m
a = Counter(y)
b = Counter(dm)
if a == b:
    print("yes")
else:
    print("no")