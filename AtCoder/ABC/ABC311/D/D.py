'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc311/tasks/abc311_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc311/tasks/abc311_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import deque

def main():
    n, m =  map(int, input().split())
    s = [input() for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    is_ok = [[[0 for _ in range(5)] for _ in range(200)] for _ in range(200)]
    is_ok[1][1][4] = 1
    q = deque()
    q.append((1, 1, 4))
    while q:
        x, y, dir_ = q.popleft()
        if dir_ == 4:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if s[nx][ny] == '#':
                    if not is_ok[x][y][4]:
                        is_ok[x][y][4] = 1
                        q.append((x, y, 4))
                else:
                    if not is_ok[nx][ny][i]:
                        is_ok[nx][ny][i] = 1
                        q.append((nx, ny, i))
        else:
            nx = x + dx[dir_]
            ny = y + dy[dir_]
            if s[nx][ny] == '#':
                if not is_ok[x][y][4]:
                    is_ok[x][y][4] = 1
                    q.append((x, y, 4))
            else:
                if not is_ok[nx][ny][dir_]:
                    is_ok[nx][ny][dir_] = 1
                    q.append((nx, ny, dir_))
    ans = 0
    for i in range(n):
        for j in range(m):
            cnt = any(is_ok[i][j])
            ans += cnt

    print(ans)

if __name__ == "__main__":
    main()