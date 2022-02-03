n = int(input())
num = []
for i in range(n):
    a = int(input())
    if a not in num:
        num.add(a)
    elif a in num:
        num.remove(a)
print(len(num))