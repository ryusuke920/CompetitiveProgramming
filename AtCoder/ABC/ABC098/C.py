n = int(input())
s = input()
e = s.count("E")
w = n - e
ans = 10**9
if s[0] == "W":
    cnt = e
else:
    cnt = e-1
num = cnt
for i in range(n-1):
    if s[i] == s[i+1] and s[i] == "E":
        cnt -= 1
    elif s[i] == s[i+1]:
        cnt += 1
    ans = min(ans,cnt,num)
    ans = max(ans,0)
print(max(ans,0))