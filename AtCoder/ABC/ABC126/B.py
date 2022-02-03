s = str(input())
a = int(s[0])*10 + int(s[1])
b = int(s[2])*10 + int(s[3])
if 1 <= a <= 12 and 1 <= b <= 12:
    print("AMBIGUOUS")
elif 1 <= a <= 12:
    print("MMYY")
elif 1 <= b <= 12:
    print("YYMM")
else:
    print("NA")