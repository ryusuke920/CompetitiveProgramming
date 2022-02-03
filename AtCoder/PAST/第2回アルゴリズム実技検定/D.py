s = input()
word = set()
for i in range(min(3, len(s))):
    for j in range(len(s) - i):
        word.add(s[j:j + i + 1])

word = list(word)
ans = set()

from itertools import product
for i in word:
    for j in product([0, 1], repeat=len(i)):
        t = [w for w in i]
        for k in range(len(i)):
            if j[k] == 1:
                t[k] = "."
        ans.add("".join(t))

print(len(ans))