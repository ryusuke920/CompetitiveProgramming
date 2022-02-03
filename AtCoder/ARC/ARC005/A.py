n = int(input())
s = input().split()
ans = ["TAKAHASHIKUN", "Takahashikun", "takahashikun", "TAKAHASHIKUN.", "Takahashikun.", "takahashikun."]
count = 0
for i in s:
    if i in ans:
        count += 1
print(count)