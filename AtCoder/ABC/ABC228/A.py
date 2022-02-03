s, t, x = map(int,input().split())
if s < t:
    print("Yes") if s <= x < t else print("No")
else:
    s, t = t, s
    print("No") if s <= x < t else print("Yes")