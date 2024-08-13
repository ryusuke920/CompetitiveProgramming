'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc347/tasks/abc347_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc347/tasks/abc347_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    r = [[] for _ in range(n)]
    for i in range(q):
        r[x[i] - 1].append(i)
    print(*r,sep="\n")
    
    for i in range(n):
        if len(r[i]) % 2 == 1:
            r[i].append(q)
    
    # print(*r,sep="\n")
    sum_ = [0]*(q + 1)
    p = set()
    for i in range(q):
        # len_ += 1
        if x[i] - 1 in p:
            p.remove(x[i] - 1)
        else:
            p.add(x[i] - 1)
        sum_[i + 1] += sum_[i] + len(p)
    
    ans = []
    for i in range(n):
        cnt = 0
        for j in range(0, len(r[i]), 2):
            cnt += sum_[r[i][j + 1]] - sum_[r[i][j]]
            # cnt += sum_[r[i][j]] - sum_[r[i][j - 1]]
        ans.append(cnt)
    
    print(*ans)


if __name__ == "__main__":
    main()