s = input()    
n = len(s) // 2 
if  s[:n] == s[-n:]:
    print("Yes")
else :
    print("No")