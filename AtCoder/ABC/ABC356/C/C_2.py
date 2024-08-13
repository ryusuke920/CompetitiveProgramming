N, M, K = map(int, input().split())
C = []
A = []
R = ""

for i in range(M):
    S = input().split()
    C.append(int(S[0]))
    a = []
    for j in range(int(S[0])):
        a.append(int(S[j + 1]))
    A.append(a)
    R += S[-1]
    # R += S[int(S[0]) + 1]

# print(C)
# print(A, sep="\n")
# print(R)

from itertools import product

ans = 0
"""
2^N * M * N = 2^15 * 100 * 15 = 1500*(1024*32) = 1.5*10^6*32
= 4/5*10^7
"""

for i in product([0, 1], repeat=N):
    flag = True # 条件を満たしているかどうかを管理するフラグ
    for j in range(M):
        is_correct = 0 # 正しい鍵が何本あるかを管理する変数
        for k in range(C[j]):
            key = A[j][k] - 1 # j 個目のテストの先頭から k 個目の鍵
            # 正しい鍵の場合の処理
            if i[key]:
                is_correct += 1
        if is_correct >= K and R[j] == "x":
            flag = False
        if is_correct < K and R[j] == "o":
            flag = False
    if flag:
        ans += 1

print(ans)