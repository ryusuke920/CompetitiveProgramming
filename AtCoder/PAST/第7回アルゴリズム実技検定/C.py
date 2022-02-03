s = input()
l, r = map(int,input().split())
if len(s) == len(str(int(s))) and l <= int(s) <= r:
    print("Yes")
else:
    print("No")