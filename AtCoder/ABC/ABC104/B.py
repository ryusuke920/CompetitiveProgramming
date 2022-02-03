s = str(input())
c = s[2:-1].count("C")
if (s[1:s.find("C")]+s[s.find("C")+1:]).islower():
    count = 1
else:
    count = 0
if s[0] == "A" and count == 1 and c == 1:
    print("AC")
else:
    print("WA")