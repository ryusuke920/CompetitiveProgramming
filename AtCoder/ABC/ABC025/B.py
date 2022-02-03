n,a,b = map(int,input().split())
ans = 0 
for i in range(n):
    s,d = map(str,input().split())
    d = int(d)
    if a <= d <= b and s[0] == "E":
        ans += d
    elif a <= d <= b and s[0] == "W":
        ans -= d
    elif d < a and s[0] == "E":
        ans += a
    elif d < a and s[0] == "W":
        ans -= a
    elif d > b and s[0] == "E":
        ans += b
    else:
        ans -= b
if ans > 0:
    print("East",ans)
elif ans < 0:
    print("West",-ans)
else:
    print(0)