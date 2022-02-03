s = input()
ch = 0
for i in range(len(s)-1):
    if s[i+1] != "9":
        ch = 1
        break
cnt = 9*(len(s)-1)
if ch == 1:
    print(cnt + int(s[0])-1)
else:
    print(cnt + int(s[0]))