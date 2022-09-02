from datetime import datetime

class Rent:
    discount = 0.7
    
    plan_dict = {1:{'description': 'hourly','fare':5,'rent_duration':1},\
                 2:{'description': 'daily','fare':10,'rent_duration':24},\
                 3:{'description': 'weekly','fare':40,'rent_duration':168}}

    def __init__(self):
        self.__number_of_bikes = None
        self.__plan = None
        self.__time_of_rent = None
        self.__price = None
        self.__duration = None


    @property
    def number_of_bikes(self):
        return self.__number_of_bikes

    @number_of_bikes.setter
    def number_of_bikes(self, number_of_bikes):
        self.__number_of_bikes = number_of_bikes
    
    @property
    def time_of_rent(self):
        return self.__time_of_rent

    @time_of_rent.setter
    def time_of_rent(self, time_of_rent):
        self.__time_of_rent = time_of_rent
    
    @property
    def plan(self):
        return self.__plan

    @plan.setter
    def plan(self, plan):
        self.__plan = plan    

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, hours):
        self.__duration = hours

    def ask_number_of_bikes(bikes) -> int:
        try:
            print('\n###########  Number of bikes   ###########\n')
            print(f"\nWe currently have {bikes.total_available} bikes available\n")
            print('\nSPECIAL OFFER:\nIf you rent 3 or more bikes you are eligible\nfor the family discount of 30% over the total price\n') 
            print('\nHow many bikes would you like to rent?\n')
            
            number_of_bikes = int(input(''))
        
        except ValueError:
            print('invalid option, please type an integer number')
            
            Rent.ask_number_of_bikes(bikes)

        else:
            if number_of_bikes <= bikes.total_available:
                print(f'You selected {number_of_bikes} bikes to rent')
                
                return number_of_bikes
            
            else:
                print(f'\nYou selected {number_of_bikes} bikes to rent')
                print(f'\nUnfortunately there is only {bikes.total_available} available')
                
                Rent.ask_number_of_bikes(bikes)

    @staticmethod
    def ask_plan():
        try:
            Rent.display_plans()
            plan = int(input('\nPlease select one of the plans available'))
        
        except ValueError:
            print('\nInvalid option, please type an integer number')
            Rent.ask_plan()
        
        else:
            if plan in range(1,4):
                return plan
            
            else:
                print('\nInvalid option, please select one of the three plan available')
                Rent.ask_plan()

    
    def rent_bike(self, bikes):
        number_of_bikes = Rent.ask_number_of_bikes(bikes)

        plan = Rent.ask_plan()

        price = self.plan_dict[plan]['fare'] * number_of_bikes

        if number_of_bikes >= 3:
            price *= self.discount
        
        self.number_of_bikes = number_of_bikes
        self.plan = plan
        self.price = price
        self.time_of_rent = datetime.now()
        self.duration = self.plan_dict[plan]['rent_duration']

        print('\nYour rent was completed successfully')
        print('\nCheck out your rent information below')
        
        self.display_rent_information()
        
        bikes.total_available -= number_of_bikes        

    def return_bike(self):
        print(f'\nYou are returning {self.number_of_bikes} bikes')
        print(f'\n The duration of your rent was {self.duration} hours')
        print(f'\n Your total to be paid is: {self.price}')



    @staticmethod
    def display_plans():
        print('\n###########  Plans available   ###########\n')
        print("1) Hourly rental: $5")
        print("2) Daily rental: $10")
        print("3) Weekly rental: $40")
    
    def display_rent_information(self):
        print('\n###########  Rent Summary   ###########\n')
        print(f"\nYour rent started at: {self.time_of_rent}")
        print(f"\nNumber of Bikes rented: {self.number_of_bikes}")
        print(f"\nRent Plan: {self.plan_dict[self.plan]['description']}")
        print(f"\nTotal to be paid ${self.price}")
        self.get_remaining_rent_time()

    def get_remaining_rent_time(self):
        t_start = self.time_of_rent
        t_now = datetime.now()
        t_duration = self.duration
        
        time_remaining = divmod(((t_duration*3600)-(t_now - t_start).total_seconds()),3600)

        if time_remaining[0] < 0:
            print(f'Your rent is expired, please return you bike(s) immediately')
        elif time_remaining[0] > 24:
            print(f'Your rent expires in {int(time_remaining[0]/24)} days, {int(time_remaining[0]%24)} hours and {int(time_remaining[1]/60)} minutes')
        else:
            print(f'Your rent expires in {int(time_remaining[0])} hours and {int(time_remaining[1]/60)} minutes')




