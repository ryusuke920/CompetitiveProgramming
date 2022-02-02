#2020/11/5
s = input()
ans = cnt = 0
ch = ["A","G","C","T"]
for i in range(len(s)):
    if s[i] in ch:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans,cnt)
print(ans)