# 9 点
s = str(input())
t = str(input())
if s == t:
    print("same")
elif s.upper() == t.upper():
    print("case-insensitive")
else:
    print("different")