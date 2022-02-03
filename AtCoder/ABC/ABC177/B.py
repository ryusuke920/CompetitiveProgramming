s = input()
t = input()
cnt = 0
ans = 0
for i in range(len(s)-len(t)+1):
    cnt = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            cnt += 1
        ans = max(cnt,ans)
print(len(t)-ans)