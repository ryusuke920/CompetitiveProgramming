'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc394/tasks/abc394_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc394/tasks/abc394_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    S = list(input())[::-1]
    N = len(S)
    ans = []
    i = 0
    while i < N:
        if i == N - 1:
            ans.append(S[i])
        else:
            if S[i] + S[i + 1] == "AW":
                ans.append("C")
                S[i + 1] = "A"
            else:
                ans.append(S[i])
        i += 1
    print("".join(ans)[::-1])

if __name__ == "__main__":
    main()