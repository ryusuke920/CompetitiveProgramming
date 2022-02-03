a,b = map(int,input().split())
count = 0
if a > 0:
    print("Positive")
elif a == 0:
    print(0)
else:
    if b >= 0:
        print("Zero")
    else:
        count = a-b+1
        if count%2 == 0:
            print("Positive")
        else:
            print("Negative")