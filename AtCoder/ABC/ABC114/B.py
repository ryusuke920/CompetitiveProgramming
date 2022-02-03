s = input()
ans = 1000
for i in range(len(s)-2):
    if ans >= abs( int(s[i])*100 + int(s[i+1])*10 + int(s[i+2]) - 753):
        ans = abs( int(s[i])*100 + int(s[i+1])*10 + int(s[i+2]) - 753)
print(ans)