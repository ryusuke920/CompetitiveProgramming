s = list(input())
ans = []
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i = 0
while i < len(s):
    cnt = ""
    if s[i] == "@":
        while True:
            i += 1
            if i >= len(s):
                break
            if s[i] in alpha:
                cnt += s[i]
            else:
                ans.append(cnt)
                break
    else:
        i += 1
if cnt != "":
    ans.append(cnt)
ans = set(ans)
word = []
for i in ans:
    if i != "":
        word.append(i)
word.sort()
print(*word, sep = "\n")