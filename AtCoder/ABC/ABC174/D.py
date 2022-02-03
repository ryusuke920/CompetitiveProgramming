n = int(input())
s = str(input())
c1 = s.count("W")
c2 = len(s) - c1
ss = s[:c2]
c3 = ss.count("W")
print(min(c1, c3))