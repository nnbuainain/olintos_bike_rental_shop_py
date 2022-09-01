import json



def menu():
    
    print('\n###########  WELCOME TO THE BIKE SHOP!   ###########\n')
    print('\n Please select an option from the menu\n')
    print("1) Rent a bike")
    print("2) Return a bike")
    print("3) See bikes available")
    print("4) Exit")
    
def main() -> bool:
    option = None
    
    while option != 4:
        menu()
        
        try:
            option = int(input())
        
        except ValueError:
            print('Invalid Option, please type a number available in the menu')
            menu()
        
        else:
            if option == 1:
                pass
            
            elif option == 2:
                pass
            
            elif option == 3:
                pass
            
            elif option == 4:
                pass

            else:
                print('Invalid Option, please type a number available in the menu')



if __name__ == '__main__':
    main()