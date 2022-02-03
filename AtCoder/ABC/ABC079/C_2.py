a,b,c,d = input()
for i in range(2**3):
    ch = ["+","+","+"]
    for j in range(3):
        if (i >> j & 1):
            ch[j] = "-"
    if eval(a+ch[0]+b+ch[1]+c+ch[2]+d) == 7:
        print(a+ch[0]+b+ch[1]+c+ch[2]+d,"=7", sep = "")
        break