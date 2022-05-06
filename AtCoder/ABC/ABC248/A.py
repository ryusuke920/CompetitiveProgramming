s = set()
for i in range(10):
    s.add(i)

t = input()
u = set()
for i in t:
    u.add(int(i))
print(str(s ^ u)[1])