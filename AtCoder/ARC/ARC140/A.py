def yakusu(n):
    ans1 = []
    ans2 = []

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans1.append(i)
            ans2.append(n//i)
    return ans2+ans1[::-1]


N, K = map(int, input().split())
S = list(input())
for v in yakusu(N):
    # v はNの約数の一つ、v個に分ける
    li = []
    block = N//v
    if v == 1:
        print(N)
        exit()
    for i in range(v):
        li.append(S[i*block:(i+1)*block])

    for i in range(len(li)):
        cnt = 0
        for j in range(len(li)):
            if i != j:
                for k in range(block):
                    if li[i][k] != li[j][k]:
                        cnt += 1

        if cnt <= K:
            print(block)
            exit()