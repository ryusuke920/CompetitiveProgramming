import math
x1,y1,r = map(int,input().split())
x2,y2,x3,y3 = map(int,input().split())
dia1 = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2) # 四角形の左下対角線
dia2 = math.sqrt(abs(x1-x3)**2 + abs(y1-y2)**2) # 四角形の右下対角線
dia3 = math.sqrt(abs(x1-x3)**2 + abs(y1-y3)**2) # 四角形の右上対角線
dia4 = math.sqrt(abs(x1-x2)**2 + abs(y1-y3)**2) # 四角形の左上対角線
if (x1-x2 >= r) and (x3-x1 >= r) and (y1-y2 >= r) and (y3-y1 >= r):
    print("NO")
    print("YES")
elif (dia1 <= r) and (dia2 <= r) and (dia3 <= r) and (dia4 <= r):
    print("YES")
    print("NO") 
else:
    print("YES")
    print("YES")