n,l = map(int,input().split())
s = str(input())
count = 0
tab = 1
for i in range(len(s)):
    if s[i] == "+":
        tab += 1
    else:
        tab -= 1
    if tab > l:
        count += 1
        tab = 1
print(count)