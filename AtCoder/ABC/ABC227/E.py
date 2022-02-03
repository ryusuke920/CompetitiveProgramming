s = list(input())
K = int(input())
l = len(s)
num = set()
num.add("".join(s))
from random import randint
for _ in range(10 ** 3):
    t = [i for i in s]
    for k in range(min(10 ** 4, K)):
        a = randint(0, l - 2)
        t[a], t[a + 1] = t[a + 1], t[a] 
        num.add("".join(t))

print(len(num))