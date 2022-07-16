from itertools import permutations

n = int(input())
s = input()

for p in permutations(range(n)):
    word = []
    for j in range(n):
        word.append(s[p[j]])
    
    word = "".join(word)
    if s != word and s != word[::-1]:
        print(word)
        exit()

print("None")