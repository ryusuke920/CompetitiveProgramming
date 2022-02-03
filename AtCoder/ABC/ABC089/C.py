from collections import Counter
n = int(input())
s = [str(input()) for _ in range(n)]
count = [0]*5
# M A R C H
for i in range(n):
    if s[i][0] == "M":
        count[0] += 1
    elif s[i][0] == "A":
        count[1] += 1
    elif s[i][0] == "R":
        count[2] += 1
    elif s[i][0] == "C":
        count[3] += 1
    elif s[i][0] == "H":
        count[4] += 1
ans = 0
ans += count[0]*count[1]*count[2]
ans += count[0]*count[1]*count[3]
ans += count[0]*count[1]*count[4]
ans += count[0]*count[2]*count[3]
ans += count[0]*count[2]*count[4]
ans += count[0]*count[3]*count[4]
ans += count[1]*count[2]*count[3]
ans += count[1]*count[2]*count[4]
ans += count[1]*count[3]*count[4]
ans += count[2]*count[3]*count[4]
print(ans)