n = int(input())
cnt = [0,1,2,3,4,5,6,7,8,9]
num = 0
ans = 0
keta = 2
while True:
    if keta > len(str(n)):
        break

    if keta == 2:
        for i in range(10):
            num = int(str(cnt[i]) + str(cnt[i]))
            if len(str(num)) != 2:continue
            if num <= n:
                ans += 1
    elif keta == 4:
        for i in range(10):
            for j in range(10):
                num = str(cnt[i]) + str(cnt[j])
                num = int(num + num)

                if len(str(num)) != 4:continue
                if num <= n:
                    ans += 1
    elif keta == 6:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    num = str(cnt[i]) + str(cnt[j]) + str(cnt[k])
                    num = int(num + num)
                    if len(str(num)) != 6:continue
                    if num <= n:
                        ans += 1
    elif keta == 8:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        num = str(cnt[i]) + str(cnt[j]) + str(cnt[k]) + str(cnt[l])
                        num = int(num + num)
                        if len(str(num)) != 8:continue
                        if num <= n:
                            ans += 1
    elif keta == 10:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        for m in range(10):
                            num = str(cnt[i]) + str(cnt[j]) + str(cnt[k]) + str(cnt[l]) + str(cnt[m])
                            num = int(num + num)
                            if len(str(num)) != 10:continue
                            if num <= n:
                                ans += 1
    elif keta == 12:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        for m in range(10):
                            for z in range(10):
                                num = str(cnt[i]) + str(cnt[j]) + str(cnt[k]) + str(cnt[l]) + str(cnt[m]) + str(cnt[z])
                                num = int(num + num)
                                if len(str(num)) != 12:continue
                                if num <= n:
                                    ans += 1
    keta += 2
print(ans)