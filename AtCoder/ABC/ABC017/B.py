x = str(input())
#ch, o, k, uのいずれか
while True:
    if len(x) == 0:
        print("YES")
        break
    if x[0] == "o" or x[0] == "k" or x[0] == "u":
        x = x[1:]
    elif (x[0] == "c" and x[1] == "h"):
        x = x[2:]
    else:
        print("NO")
        break