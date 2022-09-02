from models.bikes import Bikes
from models.rent import Rent


def menu():
    
    print("\n###########  WELCOME TO OLINTO'S BIKE SHOP!   ###########\n")
    print('\n Please select an option from the menu\n')
    print("1) Rent bike")
    print("2) Return bike")
    print("3) See bikes available")
    print("4) Exit")

    
def main() -> bool:
    option = None
    bikes = Bikes()

    while option != 4:
        menu()
        
        try:
            option = int(input())
        
        except ValueError:
            print('Invalid Option, please type a number available in the menu')
            
            menu()
        
        else:
            if option == 1:
                rent = Rent() 
                
                rent.rent_bike(bikes)
            
            elif option == 2:
                rent.return_bikes(bikes)
                
            elif option == 3:
                bikes.list_bikes_available()
            
            elif option == 4:
                print('\nExiting the app...')
                print('See ya later!')

            else:
                print('Invalid Option, please type a number available in the menu')


if __name__ == '__main__':
    main()