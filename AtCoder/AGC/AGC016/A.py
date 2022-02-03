from collections import Counter
s = input()
x = Counter(s).most_common()
ans = 1000
for i in range(len(x)):
    word = x[i][0]
    num = t = 0
    for j in range(len(s)):
        if word == s[j]:
            num = max(num, t)
            t = 0
        else:
            t += 1
    ans = min(ans, max(num, t))
print(ans)