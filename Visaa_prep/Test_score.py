n,m,p=map(int,input().split())
if p % m == 0 and p//m<=n:
    print("YES")
else:
    print("NO")
