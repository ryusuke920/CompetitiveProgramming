'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc177/tasks/arc177_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/arc177/tasks/arc177_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    N = int(input())
    S = input()
    t = ""
    for i in reversed(range(N)):
        if S[i] == "1":
            t += ("A"*(i + 1)) + ("B"*i)
    
    print(len(t))
    print(t)


if __name__ == "__main__":
    main()