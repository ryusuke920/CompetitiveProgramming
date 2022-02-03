s = str(input())
num = ["0","1","2","3","4","5","6","7","8","9"]
ans = []
for i in s:
    if i in num:
        ans.append(str(i))
print(*ans,sep = "")