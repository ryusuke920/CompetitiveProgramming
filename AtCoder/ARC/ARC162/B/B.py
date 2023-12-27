'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc162/tasks/arc162_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/arc162/tasks/arc162_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    p = list(map(int, input().split()))

    num = 0
    q = dict()
    for i in range(n):
        q[p[i]] = i + 1

    # i 番目のループで p[i]を i に持ってくる
    ans = []
    for i in range(1, n - 1):
        ind = q[i]
        if ind == i:
            continue
#        if ind <= n:
 #           ans.append((n - 1, i - 1))
        # 末尾にある場合はiとスワップ
        if ind == n:
            ans.append((n - 1, i - 1))
            ans.append((i + 1, i - 1))

            for j in range(i + 1, n + 1):
                if q[j] == ind - 1:
                    q[j] = i + 2
                elif q[j] == i:
                    q[j] += 1
                else:
                    # 右に２シフト
                    q[j] += 2
        else:
            ans.append((q[i], i - 1))
#            ans.append((q[i], i + 2))
            for j in range(i + 1, n + 1):
                if q[j] == ind + 1:
                    q[j] = i + 1
                elif q[j] < ind:
                    # 右に２シフト
                    q[j] += 2
        """
        while True:
            # 末尾にある場合
            if p[-1] == i + 1:
                ans.append((n - 1, i))
                q1 = p[:i]
                p1p2 = [p[n - 2], p[n - 1]]
                q2 = p[i + 1:]
        """

    if len(ans) <= 2 * 10**3 and q[n] == n:
        print("Yes")
        print(len(ans))
        for i, j in ans:
            print(i, j)
    else:
        print("No")


if __name__ == "__main__":
    main()