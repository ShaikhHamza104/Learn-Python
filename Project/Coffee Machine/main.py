class CoffeeMachine:
    def __init__(self):
        self.water = 0
        self.list_of_tea = ["Black Tea", "Green Tea" , "Earl Grey"]
        self.sugar = 0
        self.milk = 0
        self.coffee_beans = 0

    def menu(self):
        while True:
            print('''
Welcome to Coffee Machine

1. Add Water (ml)
2. Add Sugar (ml)
3. Add Milk (ml)
4. Add Coffee Beans
5. Clean Machine
6. Add Tea Name 
7. Get Machine Status
8. Remove tea name
9. Exit
            ''')

            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                self.addWater()
            elif user_choice == 2:
                self.addSugar()
            elif user_choice == 3:
                self.addMilk()
            elif user_choice == 4:
                self.addCoffeeBeans()
            elif user_choice == 5:
                self.cleanMachine()
            elif user_choice == 6:
                self.addTeaTypeAndName()
            elif user_choice == 7:
                self.getStatus()
            elif user_choice == 8:
                self.deleteTea()
            elif user_choice == 9:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def addWater(self):
        new_amount = int(input("How much water do you want to add (ml): "))
        self.water += new_amount
        print(f"You added {new_amount} ml of water.")

    def addSugar(self):
        new_amount = int(input("How much sugar do you want to add (ml): "))
        self.sugar += new_amount
        print(f"You added {new_amount} ml of sugar.")

    def addMilk(self):
        new_amount = int(input("How much milk do you want to add (ml): "))
        self.milk += new_amount
        print(f"You added {new_amount} ml of milk.")

    def addCoffeeBeans(self):
        new_amount = int(input("Enter the number of coffee beans: "))
        self.coffee_beans += new_amount
        print(f"You added {new_amount} coffee beans.")

    def getStatus(self):
        print(f"Current machine status:")
        print(f"\tWater: {self.water} ml")
        print(f"\tSugar: {self.sugar} ml")
        print(f"\tMilk: {self.milk} ml")
        print(f"\tCoffee Beans: {self.coffee_beans}")
        print("\nTea Types:")
        if len(self.list_of_tea)==0:
            print("List of tea is empty ")
        else:
            for tea in self.list_of_tea:
                print(tea)


    def cleanMachine(self):
        self.water = 0
        self.sugar = 0
        self.milk = 0
        self.coffee_beans = 0
        self.list_of_tea.clear()
        print("Machine cleaned!")

    def addTeaTypeAndName(self):
        name = input("Enter the name of the tea: ")
        if name not in self.list_of_tea:
            self.list_of_tea.append(name)
            print(f"Tea '{name}' added.")
        else:
            print(f"Tea {name} is already present in this machine")

    def deleteTea(self):
        tea=input("Enter tea name : ")
        if tea not in self.list_of_tea:
            print(f"{tea} is not present in this machine")
        else:
            self.list_of_tea.remove(tea)


class Customer(CoffeeMachine):
    def __init__(self):
        super.__init__()
        self.prize={

            "water":5,
            "suger":9,
            "milk":8,
            "cofee Bean":10
        }                

    def getOrder(self):
        tea_type=input("Enter the name of the tea: ").title()
        self.calculate_prize=0
        water=float(input("How much water do you want to make a coffee: (measure as cup )"))
        self.calculate_prize+=self.prize["water"]-(water*10)
        milk=float(input("How much milk do you want to make a coffee: (measure as cup )"))
        self.calculate_prize+=self.prize["milk"]-(milk*10)
        suger=float(input("How much suger do you want to make a coffee: (measure as spoone )"))
        self.calculate_prize+=self.prize["suger"]
        coffee_beans=float(input("How much coffee_beans do you want to make a coffee: (measure as quantity )"))
        self.calculate_prize+=self.prize["cofee Bean"]-(coffee_beans*100)
    def getRecipt(self):
        print(f'''{self.calculate_prize}''')
m=Customer()  
m.getOrder()
m.getRecipt()
# write a function to add two number
