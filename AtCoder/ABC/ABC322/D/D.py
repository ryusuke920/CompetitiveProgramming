n = 4
INF = 10**18

def check(s):
    t = [list(i) for i in s]
    for i in range(n):
        for j in range(n):
            t[j][n - i - 1] = s[i][j]
    return [''.join(i) for i in t]

def f(dx: int, dy: int, s, cnt):
    for i in range(n):
        for j in range(n):
            x = dx + i
            y = dy + j
            if s[i][j] == '#':
                if 0 <= x < n and 0 <= y < n:
                    cnt[x][y] += 1
                else:
                    cnt[0][0] += INF

def main():
    S = [[input() for _ in range(n)] for _ in range(3)]

    poly = [(i, j) for i in range(-3, 4) for j in range(-3, 4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ss = S[:]
                for _ in range(i):
                    ss[0] = check(ss[0])
                for _ in range(j):
                    ss[1] = check(ss[1])
                for _ in range(k):
                    ss[2] = check(ss[2])   
                len_ = len(poly)
                for ii in range(len_):
                    for jj in range(len_):
                        for kk in range(len_):
                            cnt = [[0] * n for _ in range(n)]
                            f(poly[ii][0], poly[ii][1], ss[0], cnt)
                            f(poly[jj][0], poly[jj][1], ss[1], cnt)
                            f(poly[kk][0], poly[kk][1], ss[2], cnt)
                            if all(all(cell == 1 for cell in row) for row in cnt):
                                exit(print("Yes"))               
    print("No")


if __name__ == "__main__":
    main()