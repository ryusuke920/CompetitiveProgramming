a,b = map(int,input().split())
c = a//4 - a//100 + a//400
d = b//4 - b//100 + b//400
num = 0
if a%400 == 0:
    num += 1
elif a%100 == 0:
    num += 0
elif a%4 == 0:
    num += 1
print(d-c+num)