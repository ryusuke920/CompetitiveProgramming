'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc328/tasks/abc328_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc328/tasks/abc328_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n, q = map(int, input().split())
    s = input()
    p = [0] * (n + 1)

    for i in range(1, n):
        if s[i - 1] == s[i]:
            p[i] += 1
        p[i] += p[i - 1]
    
    for _ in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
        print(p[r] - p[l])



if __name__ == "__main__":
    main()