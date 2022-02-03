n = int(input())
s = list(map(str,input().split()))
for i in range(n):
    if s[i] == "Y":
        print("Four")
        break
else:
    print("Three")