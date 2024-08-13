'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc360/tasks/abc360_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc360/tasks/abc360_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from bisect import bisect_left, bisect_right

def main() -> None:
    N, T = map(int, input().split())
    S = input()
    X = list(map(int, input().split()))

    a = []
    for i in range(N):
        if S[i] == "0":
            a.append(X[i])
    a.sort()

    ans = 0
    for i in range(N):
        if S[i] == "1":
            l = bisect_left(a, X[i])
            r = bisect_right(a, X[i] + 2*T)
            ans += r - l
    
    print(ans)


if __name__ == "__main__":
    main()