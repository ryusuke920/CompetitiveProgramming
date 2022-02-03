from collections import Counter
s = input()
t = input()
x = Counter(s)
y = Counter(t)
x = x.most_common()
y = y.most_common()
if len(x) != len(y):
    exit(print("No"))
for i in range(len(x)):
    if x[i][1] != y[i][1]:
        exit(print("No"))
print("Yes")