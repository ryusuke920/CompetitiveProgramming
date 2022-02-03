k = int(input())
t = list(input())
word = []
cnt = 0
for i in range(len(t)):
    if t[i] == "s" and cnt < k:
        cnt += 1
    else:
        word.append(t[i])
word.sort()
print(*word)