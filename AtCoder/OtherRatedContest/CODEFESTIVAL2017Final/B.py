s = input()
ans = [0] * 3
for i in range(len(s)):
    if s[i] == "a":
        ans[0] += 1
    elif s[i] == "b":
        ans[1] += 1
    else:
        ans[2] += 1

if (abs(ans[1] - ans[0]) <= 1 and abs(ans[2] - ans[0]) <= 1 and abs(ans[2] - ans[1]) <= 1):
    print("YES")
else:
    print("NO")