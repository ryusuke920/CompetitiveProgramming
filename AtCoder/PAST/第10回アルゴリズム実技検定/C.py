a = input()
l = len(a)
l -= 1
p = l // 3
q = l % 3
c = chr(96 + p)
print(a[:q + 1] + c)