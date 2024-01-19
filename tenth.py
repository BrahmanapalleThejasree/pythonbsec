a=int(input('enter value'))
b=int(input('enter value'))
c=input('enter character')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print(a**b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
else:
    print("enter arithmetic operator")