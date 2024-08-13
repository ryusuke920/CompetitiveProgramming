'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc360/tasks/abc360_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc360/tasks/abc360_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    S, T = input().split()
    l = len(S)
    for w in range(1, l):
        for c in range(w):
            cnt = []
            for i in range(l):
                if i % w == c:
                    cnt.append(S[i])
            # print(w, c, cnt)
            if "".join(cnt) == T:
                print("Yes")
                exit()
    
    print("No")



if __name__ == "__main__":
    main()