s = str(input())
ans = 0
for i in s:
    if ans == 0 and (i == "I" or i == "i"):
        ans += 1
    if ans == 1 and (i == "C" or i == "c"):
        ans += 1
    if ans == 2 and (i == "T" or i == "t"):
        print("YES")
        exit()
if ans <= 2:
    print("NO")