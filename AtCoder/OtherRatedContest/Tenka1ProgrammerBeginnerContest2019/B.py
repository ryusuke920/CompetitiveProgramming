n = int(input())
s = str(input())
k = int(input())
for i in s:
    if i != s[k-1]:
        print("*",end = "")
    else:
        print(i,end = "")