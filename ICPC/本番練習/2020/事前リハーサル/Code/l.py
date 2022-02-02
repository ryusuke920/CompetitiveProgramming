while True:
    n = int(input())
    if n == 0:
        break
    word = [input() for _ in range(n)]
    ch = 0
    cnt = 0
    ans = 0
    for i in range(n-1):
        for j in range(i,n):
            if cnt == 0 or cnt == 2:
                if len(word[j]) + cnt < 5:
                    cnt += len(word[j])
                elif len(word[j]) + cnt == 5:
                    ch += 1
                    cnt = 0
                else:
                    ans = i
                    cnt = 0
                    ch = 0
            else: # cnt = 1,3,4
                if len(word[j]) + cnt < 7:
                    cnt += len(word[j])
                elif len(word[j]) + cnt == 7:
                    ch += 1
                    cnt = 0
                else:
                    ans = i
                    cnt = 0
                    ch = 0
            if ch == 5:
                exit(print(ans+1))
        print(i,cnt,ch,word[ans])