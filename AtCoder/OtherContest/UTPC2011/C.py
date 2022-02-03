from itertools import product
s = input()
before = ""
after = ""
i = 0
while s[i] != "i":
    before += s[i]
    i += 1
i += 3
while i <= len(s) - 1:
    after += s[i]
    i += 1

word = [["(", ")"], ["{", "}"], ["[", "]"]]
ans = 3
for i in product([0, 1], repeat = len(before) + len(after)):
    x = ""
    y = ""
    for j in range(len(before) + len(after)):
        if i[j] == 1:
            if j <= len(before) - 1:
                x += before[j]
            else:
                y += after[j - len(before)]
    ch = 0
    if len(x) != len(y): continue
    for k in range(len(x)):
        if x[k] == word[0][0]:
            if y[-k - 1] != word[0][1]: ch = 1
        if x[k] == word[0][1]:
            if y[-k - 1] != word[0][0]: ch = 1
        if x[k] == word[1][0]:
            if y[-k - 1] != word[1][1]: ch = 1
        if x[k] == word[1][1]:
            if y[-k - 1] != word[1][0]: ch = 1
        if x[k] == word[2][0]:
            if y[-k - 1] != word[2][1]: ch = 1
        if x[k] == word[2][1]:
            if y[-k - 1] != word[2][0]: ch = 1
    if ch == 0:
        ans = max(ans, 3 + len(x) * 2)
print(ans)