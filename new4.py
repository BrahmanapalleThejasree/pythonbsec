num=int(input('----'))
res=0
for k in range(1,num):
    if num%k==0:
        res+=k
if res==num:
        print('perfect')
else:
        print('not perfect')        
