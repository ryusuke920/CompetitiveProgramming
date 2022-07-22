s = input()
t = input()

def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append([tmp, count])
            #ans += tmp+str(count)
            tmp = s[i]
            count = 1
    ans.append([tmp, count])
    #ans += tmp+str(count)
    return ans

ss = rle(s)
tt = rle(t)

#print(ss)
#print(tt)

if len(ss) != len(tt):
    print("No")
    exit()
else:
    for i in range(len(ss)):
        if ss[i][0] == tt[i][0]:
            if ss[i][1] == 1 and tt[i][1] == 1:
                continue
           
            if ss[i][1] == 1:
                print("No")
                exit()

            if ss[i][1] > tt[i][1]:
                exit(print("No"))

        else:
            print("No")
            exit()

print("Yes")