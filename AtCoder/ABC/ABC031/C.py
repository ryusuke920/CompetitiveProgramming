n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n): # 高橋くんが選ぶ要素
    score = []
    for j in range(n): # 青木くんが選ぶ要素

        if i == j: continue

        l = []
        for k in range(min(i, j), max(i, j) + 1): # 0index
            l.append(a[k])

        takahashi = aoki = 0

        # 奇数番目の合計が高橋君の得点、偶数番目の合計が青木君の得点
        for index, k in enumerate(l): # 0index
            if index % 2 == 1: # aoki君
                aoki += l[index]
            else: # takahashi君
                takahashi += l[index]

        score.append([takahashi, aoki])

    score.sort(key = lambda x: x[1], reverse = True)
    ans.append(score[0][0])

print(max(ans))