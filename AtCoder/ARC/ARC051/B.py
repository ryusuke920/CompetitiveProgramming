k = int(input())

fiv = [1, 1]
for i in range(40):
    fiv.append(fiv[-1] + fiv[-2])

print(fiv[k - 1], fiv[k])