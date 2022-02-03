w,h,n = map(int,input().split())
width = w*[1]
height = h*[1]

for _ in range(n):
  x,y,a = map(int,input().split())
  if a == 1:
    width[:x] = x*[0]
  elif a == 2:
    width[x:] = (w-x)*[0]
  elif a == 3:
    height[:y] = y*[0]
  else:
    height[y:] = (h-y)*[0]
 
print(width.count(1)*height.count(1))