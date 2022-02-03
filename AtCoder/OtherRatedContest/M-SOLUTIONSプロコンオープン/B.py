s = str(input())
yes = s.count("o")
if 15 - len(s) + yes >= 8:
    print("YES")
else:
    print("NO")