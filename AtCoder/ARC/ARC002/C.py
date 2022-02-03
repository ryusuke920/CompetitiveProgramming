n = int(input())
s = input()
cnt = 0
num = [0]*16

command = ["AA", "AB", "AX", "AY", "BA", "BB", "BX", "BY", "XA", "XB", "XX", "XY", "YA", "YB", "YX", "YY"]
print(num)
max_word = []
for i in range(16):
    if num[i] == max(num):
        max_word.append(command[i])
    if len(max_word) == 2:
        break
if len(max_word) == 1:
    copy = [0] * 16
    for i in range(16):
        copy[i] = num[i]
    copy.sort(reverse = True)
    if copy[1] != 0:
        for i in range(16):
            if num[i] == copy[1]:
                max_word.append(command[i])
                break
print(max_word)