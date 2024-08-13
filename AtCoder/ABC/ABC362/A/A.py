'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc362/tasks/abc362_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc362/tasks/abc362_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    R, G, B = map(int, input().split())
    C = input()

    if C == "Red":
        print(min(G, B))
    if C == "Green":
        print(min(R, B))
    if C == "Blue":
        print(min(R, G))


if __name__ == "__main__":
    main()