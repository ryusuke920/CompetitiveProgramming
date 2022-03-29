def popcount(n: int, ope: int):
    print('n=',n,'ope=',ope)
    bin_ = bin(n)[2:]
    cnt = bin_.count('1')
    num = n % cnt
    if num == 0:
        return ope
    else:
        popcount(num, ope + 1)

n = int(input())
x = list(input())
popcount(2, 1)