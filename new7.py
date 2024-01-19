a=[2,4,7,3,5]
res=[]
for b in a:
 out=1
for i in range(1,b+1):
    out*=i
    res+=[out]
    print(res)

