m = int(input())
n = m/1000
if n < 0.1:
    print("00")
elif n <= 5:
    n *= 10
    if n//10 >= 1:
        print(int(n))
    else:
        print("0",str(int(n)),sep = "")
elif n <= 30:
    print(int(n + 50))
elif n <= 70:
    print(int((n-30)//5+80))
else:
    print(89)