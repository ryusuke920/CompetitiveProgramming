n,a,b,c,d = map(int,input().split())
s = input()
if c < d:
    if "##" in s[a:d]:
        print("No")
    else:
        print("Yes")
else:
    if "##" in s[a:c]:
        print("No")
    elif "..." in s[b-2:d+1]:
        print("Yes")
    else:
        print("No")