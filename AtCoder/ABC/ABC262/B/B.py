'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc262/tasks/abc262_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc262/tasks/abc262_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, m = map(int, input().split())
    g = [[0] * n for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u][v] = 1
        g[v][u] = 1
    
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if g[i][j] and g[j][k] and g[k][i]:
                    ans += 1
    
    print(ans)
    
if __name__ == "__main__":
    main()