s = str(input())
i = 2
while True:
    s = s[:len(s)-2]
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        break
    i += 2