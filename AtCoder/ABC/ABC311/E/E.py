'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc311/tasks/abc311_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc311/tasks/abc311_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    h, w, n = map(int, input().split())
    a, b = [0] * n, [0] * n

    g = [[0] * w for _ in range(h)]
    num = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(n):
        a[i], b[i] = map(lambda x: int(x) - 1, input().split())
        g[a[i]][b[i]] += 1
    
    for i in range(h):
        for j in range(w):
            num[i + 1][j + 1] = num[i][j + 1] + num[i + 1][j] - num[i][j] + g[i][j]

    ans = 0
    INF = 10**18
    for i in range(h):
        for j in range(w):
            l, r = 0, INF
            while (abs(r - l) > 1):
                mid = (l + r) // 2
                if i + mid > h or j + mid > w:
                    r = mid
                    continue
                #num[i + 1][j + 1] = num[i][j + 1] + num[i + 1][j] - num[i][j] + g[i][j]
                cnt = num[i + mid][j + mid] - num[i][j + mid] - num[i + mid][j] + num[i][j]

                if cnt == 0:
                    l = mid
                else:
                    r = mid
            
            ans += l
    
    print(ans)


if __name__ == "__main__":
    main()