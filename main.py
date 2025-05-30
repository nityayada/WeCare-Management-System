from read import read_products
from operations import display_products, purchase_products, sell_products

def display_welcome():
    """
    Displays a welcome message for the WeCare Shop.
    
    Parameters:
        None
    
    Returns:
        None
    
    Example:
        >>> display_welcome()
        WeCare Skin Care Products
            Kamalpokhari, Kathmandu | Phone No: 9811190255
        --------------------------------------------------------------------------------
            Welcome to WeCare Management System! Have a great day!
        --------------------------------------------------------------------------------
    """
    print("\n")
    print("\n")
    print("\t \t \t \t WeCare Skin Care Products")
    print("\n")
    print("\t \t \t  Kamalpokhari, Kathmandu | Phone No: 9811190255")
    print("\n")
    print("-"*80)
    print("\t   Welcome to WeCare Management System! Have a great day!")
    print("-"*80)
    print("\n")

def main_menu():
    """
    Displays the main menu and handles user choices for the shop management system.
    

    Raises:
        ValueError: If the user enters a non-numeric choice.
    
    Example:
        >>> main_menu()
        WeCare Skin Care Products
            Kamalpokhari, Kathmandu | Phone No: 9811190255
        --------------------------------------------------------------------------------
            Welcome to WeCare Management System! Have a great day!
        --------------------------------------------------------------------------------
        ================== Main Menu ========================
        1. Display Available Products
        2. Purchase Products (Restock) from the Supplier
        3. Selling the Products to the Customer
        4. Exit from the System
        Enter your choice (1-4): 4
        Thank you for using WeCare System. Goodbye!
    """
    products = read_products()
    display_welcome()
    
    while True:
        print("\n================== Main Menu ========================")
        print("1. Display Available Products")
        print("2. Purchase Products (Restock) from the Supplier")
        print("3. Selling the Products to the Customer ")
        print("4. Exit from the System")
        
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            
            if choice == 1:
                display_products(products)
            elif choice == 2:
                purchase_products(products)
            elif choice == 3:
                sell_products(products)
            elif choice == 4:
                print("\nThank you for using WeCare System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Calling the main_menu funtion
main_menu()
