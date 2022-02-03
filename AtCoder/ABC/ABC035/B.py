s = str(input())
t = int(input())
count = s.count("?")
x = s.count("R") - s.count("L")
y = s.count("U") - s.count("D")
ans = abs(x) + abs(y)
if t == 1:
    print(ans + count)
elif t == 2:
    if len(s)%2 == 0:
        print(max(0,ans - count))
    else:
        print(max(1,ans - count))