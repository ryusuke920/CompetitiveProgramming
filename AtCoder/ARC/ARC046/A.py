n = int(input())
ans = n//9
x = n-9*ans
if x == 0:
    x = 9
if x == 9:
    print(str(x)*ans)
else:
    print(str(x)*(ans+1))