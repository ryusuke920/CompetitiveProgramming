a = int(input())
b = int(input())
c = int(input())
while True:
    if (c%a == 0 and c%b == 0):
        print(c)
        break
    c+=1 