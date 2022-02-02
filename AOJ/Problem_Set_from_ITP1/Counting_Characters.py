import sys
s = sys.stdin.read()
print(s)
ans = [0]* 26
for i in range(len(s)):
    if ord(s[i])  - 97 >= 0 and ord(s[i])  - 97 <= 25:
        ans[ord(s[i]) - 97] += 1

for i in range(26):
    print(chr(i + 97) + " : " + str(ans[i]))