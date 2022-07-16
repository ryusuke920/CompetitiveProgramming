from itertools import permutations

s = input()

l = len(s)
ans = set()
for i in permutations(range(l)):
    word = ""
    for j in range(l):
        word += s[i[j]]
    
    ans.add(word)

print(len(ans) - 1)