q,x,a=map(int,input().split())
rem=a-x
if rem >0:
    maxi=rem//q
else:
    maxi=0
print(maxi)
