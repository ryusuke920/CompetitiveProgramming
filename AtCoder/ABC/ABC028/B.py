s = str(input())
count = [0]*6
for i in s:
    if i == "A":
        count[0] += 1
    elif i == "B":
        count[1] += 1
    elif i == "C":
        count[2] += 1
    elif i == "D":
        count[3] += 1
    elif i == "E":
        count[4] += 1
    else:
        count[5] += 1
ans = ""
for i in range(6):
    ans += "".join(str(count[i]) + " ")
for i in range(len(ans)):
    if i%2 == 0:
        ans[i] == int(ans[i])
print(ans)