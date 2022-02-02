s =input()
ans = 0
word = []
n = len(s)
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for l in range(k + 1, n):
                x = s[:i] + s[i+1:j] + s[j+1:k] + s[k+1:l] + s[l+1:]
                if x not in word:
                    word.append(x)
print(len(word))