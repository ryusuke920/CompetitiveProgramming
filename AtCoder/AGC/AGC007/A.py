h,w = map(int,input().split())
ans = 0
for i in range(h):
    s = input()
    ans += s.count("#")
if  ans != h+w-1:
    print("Impossible")
else:
    print("Possible")