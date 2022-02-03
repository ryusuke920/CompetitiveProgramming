s = input()
#mod = 10 ** 9 + 7

mod = 10 ** 9 + 7
c = ch = cho = chok = choku = chokud = chokuda = chokudai = 0
for i in s:
    if i == "c":
        c += 1
    elif i == "h":
        ch += c
    elif i == "o":
        cho += ch
    elif i == "k":
        chok += cho
    elif i == "u":
        choku += chok
    elif i == "d":
        chokud += choku
    elif i == "a":
        chokuda += chokud
    elif i == "i":
        chokudai += chokuda

print(chokudai % mod)