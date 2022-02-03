import sys
input = sys.stdin.readline

def main():
    def DigitSum(num: int) -> int:
        "桁和を求める"
        num = str(num)
        digit_sum = 0
        for i in range(len(num)):
            digit_sum += int(num[i])

        return digit_sum

    def calc(x: int, y: int) -> int:
        """１の位をx, yにしたときに10以上が作れるか、また作れる時のその場合のa + bの最小値"""

        # 足して１０以上にならないとき
        if x + y < 10: return -1, -1, -1
        
        # コピーを作っておく
        num1, num2 = [0] * 9, [0] * 9
        for i in range(9):
            num1[i] = cnt1[i]
            num2[i] = cnt2[i]

        # １０以上だが、そもそも１つもないとき
        if not (num1[x - 1] >= 1 and num2[y - 1] >= 1): return -1, -1, -1
        
        # １の位の決定
        ans1, ans2 = f"{x}", f"{y}"
        num1[x - 1] -= 1
        num2[y - 1] -= 1

        # ひたすら９を作る
        # (1, 8), (2, 7), ... ,(7, 2), (8, 1)の８種類
        for i in range(8):
            if num1[i] >= 1 and num2[7 - i] >= 1:
                min_num = min(num1[i], num2[7 - i])
                ans1 = str(i + 1) * min_num + ans1
                ans2 = str(8 - i) * min_num + ans2
                num1[i] -= min_num
                num2[7 - i] -= min_num
        
        for i in range(9):
            ans1 += str(i + 1) * num1[i]
        
        for i in reversed(range(9)):
            ans2 += str(i + 1) * num2[i]
        
        ans = int(ans1) + int(ans2)
        num = DigitSum(ans)

        return num, ans1, ans2

    a = input()
    b = input()

    # len(a) < len(b)にする
    if len(a) > len(b):
        a, b = b, a

    cnt1 = [0] * 9
    cnt2 = [0] * 9
    num = set()
    for i in range(10): num.add(str(i))

    for i in a:
        if i in num:
            cnt1[int(i) - 1] += 1

    for i in b:
        if i in num:
            cnt2[int(i) - 1] += 1

    ans = 10 ** 18
    ans_x, ans_y = "", ""
    bool = False
    for i in range(1, 10):
        for j in range(1, 10):
            cnt, x, y = calc(i, j)
            if cnt == -1: continue
            if cnt < ans:
                ans = cnt
                ans_x, ans_y = x, y
                bool = True
                #print("koko",i, j, cnt, x, y, ans_x)

    #print(ans)
    if bool:
        print(ans_x)
        print(ans_y)
    else:
        print(int(a))
        print(int(b))


if __name__ == "__main__":
    main()