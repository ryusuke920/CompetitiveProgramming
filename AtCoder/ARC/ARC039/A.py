a,b = map(int,input().split())
ma = a-b
if a//100 != 9:
    ma = max(ma, 900+(a%100)-b)
elif (a%100)//10 != 9:
    ma = max(ma, 990+(a%10)-b)
else:
    ma = max(ma, 999-b)

if b//100 != 1:
    ma = max(ma, a-(100+b%100))
elif b%100//10 != 0:
    ma = max(ma, a-(100+b%10))
else:
    ma = max(ma, a-100)
print(ma)