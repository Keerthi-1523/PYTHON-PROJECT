class bym:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.a={}
        self.hall_mat=[["S" for i in range(self.col)] for j in range(self.row)]
        self.no_of_tickets = 0
    def show(self):
        print(' ',end=' ')
        for i in range(self.col):
            print(i+1,end=' ')
        print()
        for k,i in enumerate(self.hall_mat):
            print(k+1,end=' ')
            for j in i:
                print(j,end=" ")
            print(" ")

    def bookSeat(self,ro,co,li):
        
        if self.hall_mat[ro-1][co-1]!="B":
            self.hall_mat[ro-1][co-1]="B"
            self.show()
            self.no_of_tickets+=1
            if self.row*self.col>60:
                if ro<=self.row//2:
                    li["Price"]=10
                    
                else:
                    li["Price"]=8
            else:
                li["Price"]=10
            
        else:
            print("Seat is not available")
        self.a[str(ro)+" "+str(co)]=li
    
    def stats(self):
        total_income=0
        curr_income = 0
        fi_inco,se_inco=0,0
        if self.row*self.col>60:
            for i in range(1,self.row+1):
                if(i<self.row//2+1):
                    buy_count = self.hall_mat[i-1].count('B')
                    curr_income+=buy_count*10
                    total_income+=self.col*10
                else:
                    buy_count = self.hall_mat[i-1].count('B')
                    curr_income+=buy_count*8
                    total_income+=self.col*8
           
        else:
            c=0
            for i in self.hall_mat:
               c+=i.count("B")
            curr_income+=c*10
            total_income=(self.row*self.col)*10

        print("Number of Tickets Purchased",self.no_of_tickets)
        print("Percentage {0:.2f}".format(self.no_of_tickets/(self.row*self.col)*100))
        print( "Current Income",curr_income)
        print("Total Income",total_income)
        return curr_income


    def showbok(self,ro):
        try:
            print(self.a[ro])
        except:
            print("Seat is not booked")