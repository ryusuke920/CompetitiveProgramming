k = int(input())
ans = set()
def number(num: int) -> int:
    if num >= 3234566667 + 10: 
        return
    keta = num % 10 # 下１桁
    if keta == 0:
        top = (keta + 1) % 10
        under = keta
    elif keta == 9:
        top = keta
        under = (keta - 1) % 10
    else:
        top = (keta + 1) % 10
        under = (keta - 1) % 10
    num_top = int(str(num) + str(top))
    num_mid = int(str(num) + str(keta))
    num_under = int(str(num) + str(under))
    ans.add(num_top)
    ans.add(num_mid)
    ans.add(num_under)
    number(num_top)
    number(num_mid)
    number(num_under)

for i in range(10):
    ans.add(i + 1)
    number(i + 1)
ans = list(set(ans))
ans.sort()
#print(ans[:200])
print(ans[k - 1])