s = str(input())
if (int(s[0])+int(s[1])+int(s[2])+int(s[3]) == 7):
    print(s[0],"+",s[1],"+",s[2],"+",s[3],"=7",sep = "")
elif (int(s[0])+int(s[1])+int(s[2])-int(s[3]) == 7):
    print(s[0],"+",s[1],"+",s[2],"-",s[3],"=7",sep = "")
elif (int(s[0])+int(s[1])-int(s[2])+int(s[3]) == 7):
    print(s[0],"+",s[1],"-",s[2],"+",s[3],"=7",sep = "")
elif (int(s[0])+int(s[1])-int(s[2])-int(s[3]) == 7):
    print(s[0],"+",s[1],"-",s[2],"-",s[3],"=7",sep = "")
elif (int(s[0])-int(s[1])+int(s[2])+int(s[3]) == 7):
    print(s[0],"-",s[1],"+",s[2],"+",s[3],"=7",sep = "")
elif (int(s[0])-int(s[1])+int(s[2])-int(s[3]) == 7):
    print(s[0],"-",s[1],"+",s[2],"-",s[3],"=7",sep = "")
elif (int(s[0])-int(s[1])-int(s[2])+int(s[3]) == 7):
    print(s[0],"-",s[1],"-",s[2],"+",s[3],"=7",sep = "")
else:
    print(s[0],"-",s[1],"-",s[2],"-",s[3],"=7",sep = "")