s = list(input())
ans = ""
for i in s:
    if i == "0":
        ans += "0"
    elif i == "1":
        ans += "1"
    elif i == "6":
        ans += "9"
    elif i == "8":
        ans += "8"
    else:
        ans += "6"

print(ans[::-1])