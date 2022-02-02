def is_ok(k: int) -> bool:
    money = k // a * b + (k - k // a)
    if money >= c:
        return True
    else:
        return False

def binary_search(left: int, right: int) -> int:
    while abs(left - right) > 1:
        mid = (left + right) // 2

        if is_ok(mid):
            right = mid
        else:
            left = mid

    return right

a, b, c = map(int, input().split())
print(binary_search(0, 10 ** 18 + 1))

'''
c 円を超えるのが k 歳以上か
k 歳までに b 円がもらえる年数 -> k // a * b
k 歳までに 1 円がもらえる年数 -> (k - k // a)
'''