s = str(input())
t = str(input())
count = 0
for i in range(len(s)):
    if s[i] == t[i]:
        count += 1
    elif s[i] == "@" and (t[i] == "a" or t[i] == "t" or t[i] == "c" or t[i] == "o" or t[i] == "d" or t[i] == "e" or t[i] == "r"):
        count += 1
    elif t[i] == "@" and (s[i] == "a" or s[i] == "t" or s[i] == "c" or s[i] == "o" or s[i] == "d" or s[i] == "e" or s[i] == "r"):
        count += 1
if count == len(s):
    print("You can win")
else:
    print("You will lose")