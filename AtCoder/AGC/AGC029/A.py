s = input()
ans = 0
ch = 0
for i in range(len(s)):
    if s[i] == "W":
        ans += i - ch
        ch += 1
print(ans)