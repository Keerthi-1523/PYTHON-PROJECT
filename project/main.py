from bym import *
if __name__ == "__main__":
   
       
    r_o=int(input("Enter no of rows"))
    c_o=int(input("Enter no of column"))
    a_obj=bym(r_o,c_o)
    while True:

        print("1.Show the seats")
        print("2. Buy a Ticket")
        print("3. Statistics")
        print("4.Show Booked Tickets User Info")
        print("0. Exit")
        b_in=input("Choose an option")

        if b_in=="1":
            a_obj.show()
        elif b_in=="2":
            b_r,b_c=map(int,input("ENter booking seat").split())
            li={}
            a_list=['Name','Gender','Age','Phone',"Price"]
            for i in range(4):
                li[a_list[i]]=input(a_list[i])
            li[a_list[-1]]=0
            try:
                a_obj.bookSeat(b_r,b_c,li)
            except IndexError as e:
                print("Seat Number not available")

        elif b_in=='3':
            a_obj.stats()

        elif b_in=='4':
            a_obj.showbok(input("Enter row and col with space"))

        elif b_in=='0':
            break
