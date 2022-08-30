'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc263/tasks/abc263_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc263/tasks/abc263_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

# このセグ木はPythonだとTLEするのでPyPyを推奨します

"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""
def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y など"
    return x ^ y

"""
〜単位元の一覧について〜
最小値：float("inf")
最大値：-float("inf")
XOR：0
区間和：0
区間積：1
最大公約数：0
"""
ide_ele = 0 # 初期値（単位元）の設定

class SegTree:
    def __init__(self, segfunc, init_val, ide_ele):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 2 ** n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = self.segfunc(self.seg[k], x)
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, l, r):
        " l は0index, r は1index"
        if r <= l:
            return self.ide_ele
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele
        while r - l > 1:
            if l & 1 == 0:
                res = self.segfunc(res, self.seg[l])
            if r & 1 == 1:
                res = self.segfunc(res, self.seg[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self.segfunc(res, self.seg[l])
        else:
            res = self.segfunc(res, self.segfunc(self.seg[l], self.seg[r]))
        return res


def main() -> None:
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    seg = SegTree(segfunc, a, ide_ele) # オブジェクトの作成
    ans = seg.


    print(ans)


if __name__ == "__main__":
    main()