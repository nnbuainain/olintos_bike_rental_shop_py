from models.bikes import Bikes
from models.rent import Rent


def menu():
    
    print("\n###########  WELCOME TO OLINTO'S BIKE SHOP!   ###########\n")
    print('\n Please select an option from the menu\n')
    print("1) Rent bike")
    print("2) Return bike")
    print("3) See bikes available")
    print("4) See your rent summary information")
    print("5) Exit")

    
def main() -> bool:
    option = None
    bikes = Bikes()
    rent = Rent() 
    while option != 5:
        menu()
        
        try:
            option = int(input())
        
        except ValueError:
            print('Invalid Option, please type a number available in the menu')
            
            menu()
        
        else:
            if option == 1:                
                rent.rent_bike(bikes)
            
            elif option == 2:
                rent = rent.return_bikes(bikes)
                
            elif option == 3:
                bikes.list_bikes_available()
            
            elif option == 4:
                rent.display_rent_information()

            elif option == 5:
                print('\nExiting the app...')
                print('See ya later!')

            else:
                print('Invalid Option, please type a number available in the menu')


if __name__ == '__main__':
    main()