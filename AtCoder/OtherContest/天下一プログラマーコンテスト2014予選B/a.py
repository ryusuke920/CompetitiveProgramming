s = input()
ch = "HAGIXILE" #8文字
for i in range(len(s)-6+1):
    if s[i:i+6] == "HAGIYA":
        print(s[:i]+ch+s[i+6:])