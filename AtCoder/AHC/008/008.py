import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    n = int(input()) # ペット (10 <= n <= 20)
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        a[i][0] -= 1
        a[i][1] -= 1
    m = int(input()) # 人間 (5 <= m <= 10)
    b = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    done = defaultdict(int)
    for i in range(n):
        done[f'{a[i][0]}_{a[i][1]}'] = 1
    for i in range(m):
        done[f'{b[i][0]}_{b[i][1]}'] = 1
    
    d = ((1, 0), (-1, 0), (0, 1), (0, -1)) # D, U, R, L
    commands = []
    for dy, dx in d:
        command = ''
        for i in range(m):
            now_x, now_y = b[i][0] + dy, b[i][1] + dx
            if done[f'{now_x}_{now_y}'] != 1:
                if (dy, dx) == (1, 0):
                    command += 'u'
                if (dy, dx) == (-1, 0):
                    command += 'd'
                if (dy, dx) == (0, 1):
                    command += 'r'
                if (dy, dx) == (0, -1):
                    command += 'l'
            else:
                command += '.'
        
        commands.append(command)
    
    for _ in range(296):
        commands.append('.' * m)
    
    for command in commands:
        print(*command, sep='')



if __name__ == '__main__':
    main()