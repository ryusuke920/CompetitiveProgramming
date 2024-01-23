'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc337/tasks/abc337_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc337/tasks/abc337_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    m = 0
    n -= 1
    # m * (m - 1)
    const = n
    while n:
        m += 1
        n //= 2
    print(m, flush=True)
    num = [[] for _ in range(m)]
    for i in range(const + 1):
        for j in range(m):
            #if i % 2 == 0:
            if i & (1 << j):
                num[j].append(i)
    for i in range(m):
        print(len(num[i]), end=' ', flush=True)
        for v in num[i]:
            print(v + 1, end=' ', flush=True)
        print(flush=True)
    print(flush=True)
    s = input()
    ans = 0
    for i in range(m):
        if s[i] == '1':
            ans += (1 << i)
    print(ans + 1, flush=True)


if __name__ == "__main__":
    main()
