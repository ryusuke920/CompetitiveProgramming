n = int(input())
s = [str(input()) for _ in range(n)]
ans = [0]*4
for i in range(len(s)):
    if s[i] == "AC":
        ans[0] += 1
    elif s[i] == "WA":
        ans[1] += 1
    elif s[i] == "TLE":
        ans[2] += 1
    else:
        ans[3] += 1

print("AC x ",ans[0])
print("WA x ",ans[1])
print("TLE x ",ans[2])
print("RE x ",ans[3])