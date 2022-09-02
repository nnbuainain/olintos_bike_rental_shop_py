from datetime import datetime
#from bikes import Bikes
from models.bikes import Bikes
import math
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
    def duration(self, duration: datetime):
        self.__duration = duration

    
    def rent_bike(self, bikes: Bikes):
        if self.number_of_bikes == None:
            number_of_bikes = Rent.ask_number_of_bikes(bikes)
            
            plan = Rent.ask_plan()

            price = self.plan_dict[plan]['fare'] * number_of_bikes

            if number_of_bikes >= 3:
                price *= self.discount
            
            self.number_of_bikes = number_of_bikes
            self.plan = plan
            self.price = price
            self.time_of_rent = datetime.now()
            self.duration = datetime.now() - self.time_of_rent

            print('\nYour rent was completed successfully')
            print('\nCheck out your rent information below')
            
            self.display_rent_information()
            
            bikes.total_available -= number_of_bikes        
        
        else:
            print(f'\nYou currently have {self.number_of_bikes} bikes rented')
            print('\nPlease return your bikes before making a new rent')
    

    def return_bikes(self, bikes: Bikes):
        if self.number_of_bikes != None:
            self.update_duration_and_price()
            
            print(f'\nYou are returning {self.number_of_bikes} bike(s)')
            print(f'\n The duration of your rent was {self.duration}')
            print(f'\n Your total to be paid is: {self.price}')

            bikes.total_available += self.number_of_bikes
        
        else:
            print("\n You don't currently have any bikes rented")
        
        return Rent()


    def ask_number_of_bikes(bikes: Bikes) -> int:
        try:
            print('\n###########  Number of bikes   ###########\n')
            print(f"\nWe currently have {bikes.total_available} bikes available\n")
            print('\nSPECIAL OFFER:\nIf you rent 3 or more bikes you are eligible\nfor the family discount of 30% over the total price\n') 
            print('\nHow many bikes would you like to rent?\n')
            
            number_of_bikes = int(input(''))

            if number_of_bikes < 0:
                print('\nInvalid Number Please type a positive integer number')
                
                number_of_bikes = Rent.ask_number_of_bikes(bikes)

        except ValueError:
            print('invalid option, please type an integer number')
            
            number_of_bikes = Rent.ask_number_of_bikes(bikes)

        else:
            if number_of_bikes <= bikes.total_available:
                print(f'You selected {number_of_bikes} bikes to rent')
            
            else:
                print(f'\nYou selected {number_of_bikes} bikes to rent')
                print(f'\nUnfortunately there is only {bikes.total_available} available')
                
                number_of_bikes = Rent.ask_number_of_bikes(bikes)
                
            return number_of_bikes


    @staticmethod
    def ask_plan():
        try:
            Rent.display_plans()
            plan = int(input('\nPlease select one of the plans available'))
        
        except ValueError:
            print('\nInvalid option, please type an integer number')
            plan = Rent.ask_plan()
            
        
        else:
            if plan not in range(1,4):
                print('\nInvalid option, please select one of the three plan available')
                plan = Rent.ask_plan()
        
        return plan

    def update_duration_and_price(self):        
        self.duration = datetime.now()-self.time_of_rent
        
        duration_in_hours = self.duration.total_seconds()/3600
        duration_of_plan = self.plan_dict[self.plan]['rent_duration']
        
        if duration_in_hours > duration_of_plan:
            rent_quotas = math.ceil(duration_in_hours/self.plan_dict[self.plan]['rent_duration'])
            
            self.price = self.plan_dict[self.plan]['fare'] * rent_quotas * self.number_of_bikes

            if self.number_of_bikes >= 3:
                self.price *= self.discount
    

    def display_rent_information(self):
        if self.number_of_bikes != None:
            self.update_duration_and_price()
            
            print('\n###########  Rent Summary   ###########\n')
            print(f"\nYour rent started at: {self.time_of_rent}")
            print(f"\nYour rent duration is: {self.duration}")
            print(f"\nNumber of Bikes rented: {self.number_of_bikes}")
            print(f"\nRent Plan: {self.plan_dict[self.plan]['description']}")
            print(f"\nTotal to be paid ${self.price}")
        
        else:
            print("\n You don't currently have any bikes rented")

    @staticmethod
    def display_plans():
        print('\n###########  Plans available   ###########\n')
        print("1) Hourly rental: $5")
        print("2) Daily rental: $10")
        print("3) Weekly rental: $40")

#import json

#from bikes import Bikes
#bikes = Bikes()
##rent = Rent()
#rent.rent_bike(bikes)

#jsonStr = json.dumps(rent.__dict__,indent=4, sort_keys=True, default=str)
#datetime.fromisoformat('2022-09-02 10:43:21.012527')
#print(jsonStr)

