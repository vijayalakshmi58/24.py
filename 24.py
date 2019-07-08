# 24.py
v=int(input())
r =[]
r=list(map(int,input('').split()))
r.sort()
for i in range(0,v,1):
  print(r[i],end=' ')
