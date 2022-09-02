from datetime import datetime
from models.bikes import Bikes
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
    def plan(self, plan: int):
        self.__plan = plan    

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, hours: int):
        self.__duration = hours

    
    def rent_bike(self, bikes: Bikes):
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

    
    def return_bikes(self, bikes: Bikes):
        self.update_duration_and_price()
        
        print(f'\nYou are returning {self.number_of_bikes} bikes')
        print(f'\n The duration of your rent was {self.duration} hour(s)')
        print(f'\n Your total to be paid is: {self.price}')

        bikes.total_available += self.number_of_bikes


    def ask_number_of_bikes(bikes: Bikes) -> int:
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


    def update_duration_and_price(self):        
        if self.duration != 1:
            self.duration = int((datetime.now()-self.time_of_rent).total_seconds()/3600)

            self.price = self.plan_dict[self.plan]['fare'] * self.number_of_bikes * self.duration

            if self.number_of_bikes >= 3:
                self.price *= self.discount
    

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


    @staticmethod
    def display_plans():
        print('\n###########  Plans available   ###########\n')
        print("1) Hourly rental: $5")
        print("2) Daily rental: $10")
        print("3) Weekly rental: $40")


#import json

#from bikes import Bikes
#bikes = Bikes()
#rent = Rent()
#rent.rent_bike(bikes)


#jsonStr = json.dumps(rent.__dict__,indent=4, sort_keys=True, default=str)
#datetime.fromisoformat('2022-09-02 10:43:21.012527')
#print(jsonStr)

