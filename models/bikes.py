class Bikes:
    def __init__(self):
        self.__total_available = 100

    @property
    def total_available(self):
        return self.__total_available
    
    @total_available.setter
    def total_available(self, number: int):
        self.__total_available = number
    
    def list_bikes_available(self):
        if self.total_available != 1:
            print(f'\nThere are {self.total_available} bikes available')
        
        else:
            print(f'\nThere is only 1 bike available')

