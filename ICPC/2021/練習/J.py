# http://icpc.yamagula.ic.i.u-tokyo.ac.jp/icpc2021/rehearsal/all_ja.html
while True:
    n = int(input())
    if n == 0:
        exit()
    a = list(map(int,input().split()))
    print(max(a))