n = int(input())
if n >= 2018:
  print(n - 2015)
elif 2016 >= n >=2015:
  print(n - 2014)
elif n == 2017 or n <= 2014:
  print(-1)