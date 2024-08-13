'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc305/tasks/abc305_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc305/tasks/abc305_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    max_ = [0]*2
    h = []
    for i in range(H):
        cnt = 0
        for j in range(W):
            cnt += S[i][j] == "#"
        if cnt != 0:
            max_[0] = max(max_[0], cnt)
            h.append((i, cnt))

    w = []
    for j in range(W):
        cnt = 0
        for i in range(H):
            cnt += S[i][j] == "#"
        if cnt != 0:
            max_[1] = max(max_[1], cnt)
            w.append((i, cnt))

    ans = []
    for i in range(H):
        cnt = 0
        for j in range(W):
            cnt += S[i][j] == "#"
        if cnt != 0 and max_[0] != cnt:
            ans.append(i + 1)
    for j in range(W):
        cnt = 0
        for i in range(H):
            cnt += S[i][j] == "#"
        if cnt != 0 and max_[1] != cnt:
            ans.append(j + 1)
    
    print(*ans)


if __name__ == "__main__":
    main()