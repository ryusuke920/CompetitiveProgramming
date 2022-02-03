a = input()
b = int(input())

if b % 2 == 0: print(a + '0' + str(b // 2))
else: print(a + '0' + str(b * 10 // 2))