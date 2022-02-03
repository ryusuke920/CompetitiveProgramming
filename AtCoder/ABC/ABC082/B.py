s = sorted(list(input()))
t = list(input())
t.sort(reverse = True)
s += "".join(s)
t += "".join(t)
if s < t:
    print("Yes")
else:
    print("No")