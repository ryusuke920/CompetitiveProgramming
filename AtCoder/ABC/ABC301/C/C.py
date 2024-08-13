'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc301/tasks/abc301_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc301/tasks/abc301_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    S = input()
    T = input()
    card = "@atcoder"
    s = S.count("@")
    t = T.count("@")
    for i in range(26):
        x = chr(ord("a") + i)
        p = S.count(x)
        q = T.count(x)
        if p != q:
            if x not in "atcoder":
                exit(print("No"))
            else:
                if p > q:
                    t -= (p - q)
                    if t < 0:
                        exit(print("No"))
                if p < q:
                    s -= (q - p)
                    if s < 0:
                        exit(print("No"))
    
    print("Yes")

if __name__ == "__main__":
    main()