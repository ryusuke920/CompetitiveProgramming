h,w = map(int,input().split())
s = [list(input().split()) for _ in range(h)]
ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = "snuke"
for i in range(h):
    for j in range(w):
        if s[i][j] == word:
            print(ch[j],i+1,sep = "")
            break