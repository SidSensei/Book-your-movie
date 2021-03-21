class cinema():
    
    global booked_seats
    booked_seats = []
    global row
    row=[]
    global column
    column=[]
    global total_collection
    total_collection=[]
    global customer_details
    customer_details = []
    
    def __init__(self):
        pass
    
    def buy_a_ticket(self):
        

        
        print('\n')
        print('Please choose seats')        
        print('\n')
        print('Enter row number')
        
        

        row_num = int(input())

        print('\n')

        print('Enter column number')

        col_num = int(input())

        print('\n')

        r1 = x//2

        
        seat = ((row_num),(col_num))

        collection = 0
        

        if seat not in booked_seats:


            if (x*y) <= 60:
                print('Price is 10$ per ticket')
                price='10$'
                collection+=10

            else:
                if row_num > (r1):
                    print('Price is 8$ per ticket')

                else:
                    print('Price is 10$ per ticket')
            

            print('\n')        

            print('Do you want to book tickets ?')
            print('\n')
            print('    y or n')

            ans = input()
            print('\n')
            
            details = {'Name':' ','Age':' ','Gender':' ','Ticket price':' ','Phone number':' '}

            if ans == ('y'):
                if row_num > (r1):
                    price='8$'
                    collection+=8

                else:
                    price='10$'
                    collection+=10
                
                total_collection.append(collection)
                row.append(row_num)
                column.append(col_num)
                booked_seats.append(seat)
                print('Enter you Name')
                details['Name']= input()
                print('Enter you Age')
                details['Age']= input()
                print('Enter you Gender')      
                details['Gender']= input()
                print('Enter you Phone number')      
                details['Phone number']= input()
                details['Ticket price']= price
                print('\n')
                print('Congratulaions, your seat is booked')
                customer_details.append(details)
            else:
                pass
        else:
            print('This seat is already booked, Please try another')
            
            
            
    def seat_layout(self):
        
        for i in range(0,c):
            if i==0:
                print('  ',end=" ")
            else:
                print(i, end=" ")

        for i in range(1,r):
            print('\n',i,end=' ')
            for j in range(1,c):
                baithak = 'S'
                for k in booked_seats:
                    if (i==k[0] and j==k[1]):
                        baithak = 'B'
                    else:
                        pass
                print(baithak, end = ' ')
        
        print('\n')
        
        
    def statistics(self):
        print('Number of prchased Tickets : ',len(booked_seats))
        print('Percentage of Tickets booked : ', round((len(booked_seats)*100)/(x*y),2))
        print('Total Income',sum(total_collection),' $')
        
        
    def user_info(self):
        for p in customer_details:
            print('\n')
            for q in p:
                print(q,' : ',p[q],' , ',end=" ")
        
        

sid = cinema()        

print('Enter the number of rows :')

x = int(input())
r=x+1

print('Enter the number of seats per rows :')

y = int(input())
c=y+1

while True:
    
#     Catalogue
    print('\n')
    print('\n Catalogue','\n 1. Seat layout','\n 2. Buy a ticket','\n 3. Statistics','\n 4. Show user info','\n 0. Exit \n')

    choice = int(input())
    
    if choice == 1:
        sid.seat_layout()
    elif choice == 2:
        sid.buy_a_ticket()
    elif choice == 3:
        sid.statistics()
    elif choice== 4:
        sid.user_info()
    elif choice == 0:
        break
