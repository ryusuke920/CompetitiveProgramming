s = input()
ans = same = 0
if len(s) % 2 == 0:
    before = s[: len(s) // 2]
    after = s[len(s) // 2 :]
    for i in range(len(before)):
        if before[i] == after[-1 - i]:
            same += 1
    if same == len(s) // 2: # 回文になる
        ans = 25 * len(s)
    elif same + 1 == len(s) // 2: # 回文になる
        ans = (25 * same * 2) + (24 * 2)
    else: 
        ans = 25 * len(s) # 回文にならない
else:
    before = s[: len(s) // 2]
    after = s[len(s) // 2 + 1 :]
    for i in range(len(before)):
        if before[i] == after[-1 - i]:
            same += 1
    if same == len(s) // 2: # 回文になる
        ans = 25 * (len(s) - 1)
    elif same + 1 == len(s) // 2: # 回文になる
        ans = (25 * same * 2) + 25 + (24 * 2)
    else: 
        ans = 25 * len(s) # 回文にならない
print(ans)