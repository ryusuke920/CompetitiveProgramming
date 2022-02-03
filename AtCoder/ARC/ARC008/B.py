from collections import Counter
import math
n, m = map(int, input().split())
name = input()
kit = input()
name_cnt = Counter(name)
kit_cnt = Counter(kit)
ans = []
for i in name_cnt:
    if kit_cnt[i] == 0:
        exit(print(-1))
    elif name_cnt[i] > kit_cnt[i]:
        ans.append(math.ceil(name_cnt[i] / kit_cnt[i]))
    else:
        ans.append(1)
print(max(ans))