s = str(input())
a = s.count("N")
b = s.count("W")
c = s.count("S")
d = s.count("E")
if (a  == 0 and c != 0) or (c  == 0 and a != 0) or (b  == 0 and d != 0) or (d  == 0 and b != 0):
    print("No")
else:
    print("Yes")