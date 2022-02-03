s = input()
k = int(input())
word = []
for i in range(len(s)):
    word.append(s[i])
for i in range(len(s) - 1):
        word.append(s[i:i + 2])
for i in range(len(s) - 2):
        word.append(s[i:i + 3])
for i in range(len(s) - 3):
        word.append(s[i:i + 4])
for i in range(len(s) - 4):
        word.append(s[i:i + 5])
word = list(set(word))
word.sort()
print(word[k - 1])