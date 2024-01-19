print('welcome to Mybus..')
dest = input(''' select destination by entering
             1 for Delhi
             2 for Mumbai
             3 for Chennai
             4 for Hyderabad:-''')
adult_seats = int(input('number of adults:-'))
child_seats = int(input('number of childrens:-'))
category    = input('enter \n 1 for AC \n 2 for Non-AC \n:-')
distance={'1':2000,'2':800,'3':350,'4':500}
if category =='1':
             adult_price=10
             child_price=5
elif category =='2':
             adult_price=5
             child_price=3
             total_price=(distance[dest]*(adult_price*adult_seats+child_price*child_seats)
                          )
             print('the total amount is:',total_price,'rupees')
confirm = input('enter "yes" for confirm or press any other key to cancell')
if confirm =='yes':
             print('your transcation successfully')
else:
             print('your transction canceled')