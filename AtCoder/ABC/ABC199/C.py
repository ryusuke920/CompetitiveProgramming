import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip()) # 2 * n
q = int(input())

turn = 0 #０が通常

for i in range(q):
    t = list(map(int,input().split()))
    if t[0] == 1:
        if turn == 0:
            s[t[1] - 1], s[t[2] - 1] = s[t[2] - 1], s[t[1] - 1]
        else:
            if t[1] <= n:
                t[1] += n
            else:
                t[1] -= n

            if t[2] <= n:
                t[2] += n
            else:
                t[2] -= n
            s[t[1] - 1], s[t[2] - 1] = s[t[2] - 1], s[t[1] - 1]
    else: # t -> 2
        if turn == 0:
            turn = 1
        else:
            turn = 0

if turn == 0:
    print(*s,sep = "")
else:
    x = s[:n]
    y = s[n:]
    s = y + x
    print(*s,sep = "")