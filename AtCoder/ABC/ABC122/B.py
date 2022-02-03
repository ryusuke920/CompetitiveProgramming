s = str(input())
ans = 0
count = 0
ch = ["A","G","C","T"]
for i in s:
    if i in ch:
        count += 1
    else:
        count = 0
    ans = max(ans,count)
print(ans)