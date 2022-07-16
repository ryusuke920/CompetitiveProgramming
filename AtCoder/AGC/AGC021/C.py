import sys
input = sys.stdin.readline


def check(y: int, x: int) -> bool:
    """ (y, x) が . であるかを判別する """
    return grid[y][x] == '.'


n, m, a, b = map(int, input().split())
A = a
B = b
grid = [['.'] * m for _ in range(n)]

# No の場合の処理
if n * m < 2 * (a + b):
    exit(print('NO'))


if n % 2 and m % 2:
    if n >= 3 and m >= 3:
        if a > 0:
            grid[-1][-1] = '>'
            grid[-1][-2] = '<'
            a -= 1
        
        if b > 0:
            grid[-1][-3] = 'v'
            grid[-2][-3] = '^'
            b -= 1
        
        if a > 0:
            grid[-3][-3] = '<'
            grid[-3][-2] = '>'
            a -= 1
        
        if b > 0:
            grid[-3][-1] = '^'
            grid[-2][-1] = 'v'
            b -= 1



# 奇数行の場合、最下段を横で埋める
if n % 2 == 1:
    for j in range(m // 2):
        if a > 0 and check(n - 1, 2 * j) and check(n - 1, 2 * j + 1):
            grid[n - 1][2 * j] = '<'
            grid[n - 1][2 * j + 1] = '>'
            a -= 1

# 奇数列の場合、最右列を縦で埋める
if m % 2 == 1:
    for i in range(n // 2):
        if b > 0 and check(2 * i, m - 1) and check(2 * i + 1, m - 1):
            grid[2 * i][m - 1] = '^'
            grid[2 * i + 1][m - 1] = 'v'
            b -= 1

# 2 * 2 で 横（A）で埋めていく
for i in range(n // 2):
    if a == 0:
        break
    sy = 2 * i
    for j in range(m // 2):
        if a == 0:
            break
        sx = 2 * j
        for ii in range(2):
            for jj in range(2):
                if a == 0:
                    break
                if jj % 2 == 0 and check(sy + ii, sx + jj) and check(sy + ii, sx + jj + 1):
                    grid[sy + ii][sx + jj] = '<'
                elif jj % 2 == 1 and grid[sy + ii][sx + jj - 1] == '<':
                    grid[sy + ii][sx + jj] = '>'
                    a -= 1

# 2 * 2 で 縦（b）で埋めていく
for i in range(n // 2):
    if b == 0:
        break
    sy = 2 * i
    for j in range(m // 2):
        if b == 0:
            break
        sx = 2 * j
        for jj in range(2):
            for ii in range(2):
                if b == 0:
                    break  
                if ii % 2 == 0 and check(sy + ii, sx + jj) and check(sy + ii + 1, sx + jj):
                    grid[sy + ii][sx + jj] = '^'
                elif ii % 2 == 1 and grid[sy + ii - 1][sx + jj] == '^':
                    grid[sy + ii][sx + jj] = 'v'
                    b -= 1

# チェック行う
x, y = x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            continue
        if grid[i][j] == '<':
            if grid[i][j + 1] == '>':
                x += 1
        if grid[i][j] == '^':
            if grid[i + 1][j] == 'v':
                y += 1

if x == A and y == B:
    print('YES')
    for i in range(n):
        print(*grid[i], sep='')
    exit()


grid = [['.'] * m for _ in range(n)]
a = A
b = B



# 奇数行の場合、最下段を横で埋める
if n % 2 == 1:
    for j in range(m // 2):
        if a > 0 and check(n - 1, 2 * j) and check(n - 1, 2 * j + 1):
            grid[n - 1][2 * j] = '<'
            grid[n - 1][2 * j + 1] = '>'
            a -= 1

# 偶数列の場合、最右列を縦で埋める
if m % 2 == 1:
    for i in range(n // 2):
        if b > 0 and check(2 * i, m - 1) and check(2 * i + 1, m - 1):
            grid[2 * i][m - 1] = '^'
            grid[2 * i + 1][m - 1] = 'v'
            b -= 1

# 2 * 2 で 横（A）で埋めていく
for i in range(n // 2):
    if a == 0:
        break
    sy = 2 * i
    for j in range(m // 2):
        if a == 0:
            break
        sx = 2 * j
        for ii in range(2):
            for jj in range(2):
                if a == 0:
                    break
                if jj % 2 == 0 and check(sy + ii, sx + jj) and check(sy + ii, sx + jj + 1):
                    grid[sy + ii][sx + jj] = '<'
                elif jj % 2 == 1 and grid[sy + ii][sx + jj - 1] == '<':
                    grid[sy + ii][sx + jj] = '>'
                    a -= 1

# 2 * 2 で 縦（b）で埋めていく
for i in range(n // 2):
    if b == 0:
        break
    sy = 2 * i
    for j in range(m // 2):
        if b == 0:
            break
        sx = 2 * j
        for jj in range(2):
            for ii in range(2):
                if b == 0:
                    break  
                if ii % 2 == 0 and check(sy + ii, sx + jj) and check(sy + ii + 1, sx + jj):
                    grid[sy + ii][sx + jj] = '^'
                elif ii % 2 == 1 and grid[sy + ii - 1][sx + jj] == '^':
                    grid[sy + ii][sx + jj] = 'v'
                    b -= 1


# チェック行う
x, y = x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            continue
        if grid[i][j] == '<':
            if grid[i][j + 1] == '>':
                x += 1
        if grid[i][j] == '^':
            if grid[i + 1][j] == 'v':
                y += 1

if x == A and y == B:
    print('YES')
    for i in range(n):
        print(*grid[i], sep='')
else:
    print("NO")