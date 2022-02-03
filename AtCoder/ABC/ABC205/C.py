a, b, c = map(int,input().split())
if (a == b) or (a + b == 0 and c % 2 == 0):
    print("=")
else:
    if c % 2 == 0: #　絶対に+
        if abs(a) > abs(b):
            print(">")
        else:
            print("<")
    elif c % 2 == 1: # -もある
        if a <= 0 and b <= 0:
            if a < b:
               print("<")
            else:
                print(">")
        elif a >= 0 and b <= 0:
            print(">")
        elif a <= 0 and b >= 0:
            print("<")
        elif a >= 0 and b >= 0:
            if a > b:
                print(">")
            else:
                print("<")