s = input()
q = int(input())
front = ""
back = ""
cnt = 0
for i in range(q):
    x = list(map(str,input().split()))
    if len(x) == 1:
        cnt += 1
    else:
        if x[1] == "1":
            if cnt%2 == 0:
                front = x[2] + front
            else:
                back = back + x[2]
        else:
            if cnt%2 == 0:
                back = back + x[2]
            else:
                front = x[2] + front 
if cnt%2 == 0:
    print(front + s + back)
else:
    print(back[::-1] + s[::-1] + front[::-1])