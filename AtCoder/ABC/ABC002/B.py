w = str(input())
ans = ""
for i in w:
    if i != "a" and i != "i" and i != "u" and i != "e" and i != "o":
        ans += "".join(i)
print(ans)