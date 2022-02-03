a,b = map(int, input().split())
ch = 0
if b*2%4 == 0:
    num = b / a
    print(num)
    if num >= 2 and num <= 4:
        ch += 1
if ch == 0:
    print("No")
else:
    print("Yes")  