a0 = 100
a1 = 100
a2 = 200
for _ in range(3,20):
    an = a0 + a1 + a2
    a0 = a1
    a1 = a2
    a2 = an
print(an)