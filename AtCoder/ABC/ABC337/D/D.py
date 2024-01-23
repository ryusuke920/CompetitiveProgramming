'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc337/tasks/abc337_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc337/tasks/abc337_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import deque

def main() -> None:
    h, w, k = map(int, input().split())
    s = [input() for _ in range(h)]
    
    INF = 10**18
    ans = INF
    
    for i in range(h):
        q = deque()
        len_ = 0
        num = 0
        for j in range(w):
            q.append(s[i][j])
            len_ += 1
            if s[i][j] == 'o':
                num += 1
            if len_ > k:
                if q[0] == 'o':
                    num -= 1
                q.popleft()
                len_ -= 1
            if s[i][j] == 'x':
                while q:
                    if q[0] == 'o':
                        num -= 1
                    q.popleft()
                    len_ -= 1
            if len_ == k:
                ans = min(ans, k - num)
    
    for i in range(w):
        q = deque()
        len_ = 0
        num = 0
        for j in range(h):
            q.append(s[j][i])
            len_ += 1
            if s[j][i] == 'o':
                num += 1
            if len_ > k:
                if q[0] == 'o':
                    num -= 1
                q.popleft()
                len_ -= 1
            if s[j][i] == 'x':
                while q:
                    if q[0] == 'o':
                        num -= 1
                    q.popleft()
                    len_ -= 1
            if len_ == k:
                ans = min(ans, k - num)
    
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()