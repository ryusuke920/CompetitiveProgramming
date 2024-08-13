'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc360/tasks/abc360_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc360/tasks/abc360_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    S = input()
    if S.index("R") < S.index("M"):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()