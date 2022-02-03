from itertools import permutations
a = list(map(int,list(input())))
l = len(a)
ans = -1
for i in permutations(a):
    for j in range(l - 1):
        x = ""
        y = ""
        for A in range(j + 1):
            x += str(i[A])
        for B in range(j + 1, l):
            y += str(i[B])
        if x[0] == "0" or y[0] == "0": continue
        ans = max(ans, int(x) * int(y))
print(ans)