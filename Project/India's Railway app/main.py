class Train:
    no_of_ticket=0
    seats=10

    list_of_train={
        222309:"Rajdhani Express",
        222310:"Shatabdi Express",
        222311:"Duronto Express",
        222312:"Garib Rath Express",
        222313:"Jan Shatabdi Express",
        222314:"Humsafar Express",
        222315:"Tejas Express",
        222316:"Vande Bharat Express",
        222317:"Gatimaan Express",
        222318:"Deccan Odyssey"}
    def __init__(self):
        while True:
            self.user_input=int(input('''
******************** WELCOME TO INDIAN'S RAILEAYS ********************
1.Display all available Trains
2.Book Ticket
3.Get stutus 
4.Add train
5.Cancel Train
6.Exit
'''))
            if self.user_input==1:
                self.displayAllTrain()
            elif self.user_input==2:
                self.bookTicket()
            elif self.user_input==3:
                self.getStatus()
            elif self.user_input==4:
                self.addTrain()        
            elif self.user_input==5:
                self.removeBook()
            elif self.user_input==6:
                break
            else:
                print("Please choose valid number not grater then 4")

    def displayAllTrain(self):
        for trainno,trainname in Train.list_of_train.items():
            print(f"{trainno}  :  {trainname}") 


    def bookTicket(self):
        self.train_no=int(input("Enter your train number "))
        if self.train_no not in self.list_of_train.keys():
            print(f"{self.train_no} train name is not avalible")
        else:
            self.destination=input("Enter your destination ")
            self.n=int(input("Enter number of ticket u want to book "))
            if self.n<=Train.seats:
                for i in range(self.n):
                    Train.seats+=1
                    Train.no_of_ticket+=1
                else:    
                    print(f"{self.no_of_ticket} Ticket has been book and your destination is {self.destination}")
            else:
                print(f"The {self.n} of seats are not avalible")


    def getStatus(self):
        self.train_no=int(input("Enter your train number "))
        if self.train_no not in Train.list_of_train.keys():
            print(f"{self.train_no} is not avalible")
        else:
            print("Train is avalible ")

    def addTrain(self):
        trainno=int(input("Enter train number : "))
        trainname=input("Enter train name : ")
        if trainname and trainno in Train.list_of_train:
            print(f"{trainname} is present in this railway")
        else:
            Train.list_of_train[trainno]=trainname

    def removeBook(self):
        trainno=int(input("Enter train number : "))
        if trainno not in Train.list_of_train:
            print(f"{trainno} is not available")
        else:
            del Train.list_of_train[trainno]
            print(f"{trainno} train is cancle ")


user=Train()