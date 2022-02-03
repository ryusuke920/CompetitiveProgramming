n = int(input())
s = str(input())
#a[]c c[]a b[]b
if s == "b":
    print(0)
    exit()

if n%2 == 0:
    print(-1)
    exit()
else:
    mid = n//2
    if s[mid] != "b":
        print(-1)
        exit()
    else:
        count = 0
        num = 0
        for i in range(1,n//2+1):
            #print(i,s[mid-i],s[mid+i])
            if num%3 == 0:
                if s[mid-i] != "a" or s[mid+i] != "c":
                    print(-1)
                    exit()
                else:
                    num += 1
            elif num%3 == 1:
                if s[mid-i] != "c" or s[mid+i] != "a":
                    print(-1)
                    exit()
                else:
                    num += 1
            else:
                if s[mid-i] != "b" or s[mid+i] != "b":
                    print(-1)
                    exit()
                else:
                    num += 1
        print(i)