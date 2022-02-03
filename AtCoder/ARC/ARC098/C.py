n = int(input())
s = input()
#     W E E W W
# 人  1 2 3 4 5
# 東  0 1 2 2 2 
# 西 0 1 1 1 2 3（人 - 東）
# ×東 2 1 0 0 0 (リーダーよりも右側)(計東 - 東)
# ×西 0 1 1 1 2 (リーダーよりも左側)
# ans 2 2 1 1 2 (×東 + ×西)
# total 東 2人

eastnum = [0]*n
westnum = [0]*(n + 1)
if s[0] == "E":
    eastnum[0] = 1
else: # s[0] == "W"
    westnum[1] = 1

for i in range(n-1):
    if s[i+1] == "E":
        eastnum[i + 1] = eastnum[i] + 1
    else:
        eastnum[i + 1] = eastnum[i]
    westnum[i + 2] = i + 2 - eastnum[i + 1]
# print(eastnum)
# print(westnum)

enum = s.count("E") # 東を向いている人のトータル人数
# >>> 2
ans = n
for i in range(n):
    eout = enum - eastnum[i]
    wout = westnum[i]
    out = eout + wout
    ans = min(ans, out)
print(ans)