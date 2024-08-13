'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc314/tasks/abc314_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc314/tasks/abc314_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    N, M = map(int, input().split())
    S = input()
    C = list(map(int, input().split()))
    g = [[] for _ in range(M)]
    for i in range(N):
        g[C[i] - 1].append(S[i])
    for i in range(M):
        g[i] = [g[i][-1]] + g[i][:-1]
    
    now = [0]*M
    ans = []
    for i in range(N):
        ans.append(g[C[i] - 1][now[C[i] - 1]])
        now[C[i] - 1] += 1

    print("".join(ans))


if __name__ == "__main__":
    main()