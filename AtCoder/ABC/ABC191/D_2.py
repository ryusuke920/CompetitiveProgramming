# 未AC
import math

def float2int(FLOAT):
    return int(FLOAT.replace(".", "")), len(FLOAT) - FLOAT.index(".") - 1

x, y, r = input().split()
ans = 0
for i in range(math.ceil(float(x) - float(r)), math.floor(float(x) + float(r)) + 1):
    b = -2 * float(y)
    c = -(r ** 2) + (i - x) ** 2 + y ** 2
    Y1 = (2 * y + math.sqrt(4 * y ** 2 - 4 * c)) / 2 # big
    Y2 = (2 * y - math.sqrt(4 * y ** 2 - 4 * c)) / 2 # small
    # A >= C
    A, B = float2int(str(Y1))
    C, D = float2int(str(Y2))
    if A / 10 ** B == C / 10 ** D:
        ans += 1
    else:
        if min(A / 10 ** B, C / 10 ** D) >= 0: # +, +
            s = math.floor(A / 10 ** B)
            t = math.ceil(C / 10 ** D)
            ans += s - t + 1
        elif (A / 10 ** B) * (C / 10 ** D) < 0: # +,-
            s = math.floor(A / 10 ** B)
            t = -math.ceil(C / 10 ** D)
            ans += s + t + 1
        else: # -, -
            s = -math.ceil(C / 10 ** D)
            t = -math.floor(A / 10 ** B)
            ans += s - t + 1
print(ans)