n = int(input())
w = list(input().split())
num = []
for i in range(len(w)):
    ans = ""
    for j in range(len(w[i])):
        if w[i][j] == 'b' or w[i][j] == 'c' or w[i][j] == 'B' or w[i][j] == 'C':
            ans += '1'
        elif w[i][j] == 'd' or w[i][j] == 'w' or w[i][j] == 'D' or w[i][j] == 'W':
            ans += '2'
        elif w[i][j] == 't' or w[i][j] == 'j' or w[i][j] == 'T' or w[i][j] == 'J':
            ans += '3'
        elif w[i][j] == 'f' or w[i][j] == 'q' or w[i][j] == 'F' or w[i][j] == 'Q':
            ans += '4'
        elif w[i][j] == 'l' or w[i][j] == 'v' or w[i][j] == 'L' or w[i][j] == 'V':
            ans += '5'
        elif w[i][j] == 's' or w[i][j] == 'x' or w[i][j] == 'S' or w[i][j] == 'X':
            ans += '6'
        elif w[i][j] == 'p' or w[i][j] == 'm' or w[i][j] == 'P' or w[i][j] == 'M':
            ans += '7'
        elif w[i][j] == 'h' or w[i][j] == 'k' or w[i][j] == 'H' or w[i][j] == 'K':
            ans += '8'
        elif w[i][j] == 'n' or w[i][j] == 'g' or w[i][j] == 'N' or w[i][j] == 'G':
            ans += '9'
        elif w[i][j] == 'z' or w[i][j] == 'r' or w[i][j] == 'Z' or w[i][j] == 'R':
            ans += '0'
    if ans == "": continue
    num.append(ans)
print(*num)