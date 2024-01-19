a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a>c:
    print('a is biggest number')
elif b>c and b>a:
      print('b is first biggestnumber')
elif c>a and c>b:
     print('c is second biggest number')
else:
    print('invaild number')
