'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc145/tasks/arc145_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/arc145/tasks/arc145_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    n = int(input())
    s = list(input())
    if s == ['B', 'A']:
        print('No')
    elif s == s[::-1]:
        print('Yes')
    else:
        print('Yes') if s[0] == 'B' or s[-1] == 'A' else print('No')

if __name__ == "__main__":
    main()