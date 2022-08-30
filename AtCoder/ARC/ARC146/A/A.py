'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc146/tasks/arc146_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/arc146/tasks/arc146_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    p = [[] for _ in range(10)]
    for i in a:
        p[len(str(i)) - 1].append(i)
    for i in range(10):
        p[i].sort(reverse=True)
    
    ans = []
    num = 0
    for i in reversed(range(10)):
        for j in p[i]:
            ans.append(str(j))
            num += 1
            if num == 3:
                t = []
                t.append(int(ans[0] + ans[1] + ans[2]))
                t.append(int(ans[0] + ans[2] + ans[1]))
                t.append(int(ans[1] + ans[0] + ans[2]))
                t.append(int(ans[1] + ans[2] + ans[0]))
                t.append(int(ans[2] + ans[0] + ans[1]))
                t.append(int(ans[2] + ans[1] + ans[0]))
                exit(print(max(t)))

if __name__ == "__main__":
    main()