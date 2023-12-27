'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc327/tasks/abc327_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc327/tasks/abc327_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    a = [list(map(int, input().split())) for _ in range(n)]
    n = 9
    is_ok = True
    for i in range(n):
        num = [0] * n
        for j in range(n):
            num[a[i][j] - 1] += 1

        flag = True
        for j in range(n):
            if num[j] != 1:
                flag = False
                break
    
    if not flag:
        is_ok = False

    for j in range(n):
        num = [0] * n
        for i in range(n):
            num[a[i][j] - 1] += 1

        flag = True
        for i in range(n):
            if num[i] != 1:
                flag = False
                break

    if not flag:
        is_ok = False
    
    # 3*3
    for i in range(3):
        for j in range(3):
            num = [0] * n
            for y in range(i * 3, 3):
                for x in range(j * 3, 3):
                    num[a[y][x] - 1] += 1
            flag = True
            for k in range(9):
                if num[k] != 1:
                    flag = False
                    break

    
    if not flag:
        is_ok = False
        
    
    print("Yes") if is_ok else print("No")


if __name__ == "__main__":
    main()