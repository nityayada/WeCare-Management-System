from datetime import datetime
import random
from write import save_products, create_purchase_invoice, create_sale_invoice
from read import pad_string

def display_products(products):
    """
    Displays available products with a 200% markup selling price.
    
    Parameters:
        products (dict): A dictionary of products with IDs as keys and details as values (see read_products).
    
    Example:
        >>> products = {
                 1: {'name': 'Moisturizer', 'brand': 'Nivea', 'quantity': 10, 'cost_price': 500.0, 'origin': 'Germany'}
             }
        >>> display_products(products)
        Available Products:
        --------------------------------------------------------------------------------
        ID     Name                 Brand           Qty        Price (NPR)    Origin
        --------------------------------------------------------------------------------
        1     |Vitamin C Serum      |Garnier        |10        |1000.0       |France
        --------------------------------------------------------------------------------
    """
    print("\nAvailable Products:")
    print("-" * 80)
    header = pad_string("ID", 5) + pad_string("Name", 21) + pad_string("Brand", 16) + \
             pad_string("Qty", 11) + pad_string("Price (NPR)", 14) + \
             pad_string("Origin", 1)
    print(header)
    print("-" * 80)
    
    for product_id, details in products.items():
        selling_price = details["cost_price"] * 2
        display_products = pad_string(product_id, 5)+ "|" + pad_string(details["name"], 20) + "|" + \
               pad_string(details["brand"], 15)+ "|" + pad_string(details["quantity"], 10)+ "|" + \
               pad_string(selling_price, 13)+ "|" + pad_string(details['origin'], 15) 
        print(display_products)
        print()
    print("-" * 80)

def purchase_products(products):
    """
    Handles purchasing products from a supplier, updating inventory and generating an invoice.
    
    Parameters:
        products (dict): A dictionary of products with IDs as keys and details as values (see read_products).
    
   
    Example:
        >>> products = {
                 1: {'name': 'Vitamin C Serum', 'brand': 'Granier',
                 'quantity': 10, 'cost_price': 500.0, 'origin': 'France'}
             }
        >>> purchase_products(products)
        Enter supplier name: Global Suppliers
        Available Products:
        --------------------------------------------------------------------------------
        ID    Name                 Brand           Qty        Price (NPR)    Origin
        --------------------------------------------------------------------------------
        1    |Vitamin C Serum     |Granier           |10         |1000.0       |France
        --------------------------------------------------------------------------------
        Please, Enter product ID to purchase (1 to finish): 1
        Please, Enter quantity to purchase: 5
        Current cost price is NPR 500.00. Enter new price or press enter to keep same: 600
        Added 5 Moisturizer to purchase list.
        Do you want to purchase more items? (yes/no): no
        [Generates and displays invoice, updates products dictionary]
    """
    print("\n------------------ Purchase Products -----------------------")
    while True:
        supplier_name = input("Please, Enter supplier name: ")
        if supplier_name == "":
            print("Please, Don't left supplier name empty\n ")
            continue
        break 
    products_purchased = []
    total_amount = 0
    purchase_loop = True
    
    while purchase_loop == True:
        display_products(products)
        
        while True:
            try:
                product_id = int(input("\nPlease, Enter product ID to purchase (1 to finish): "))
                if product_id not in products:
                    print("Invalid product ID. Please enter a valid ID.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        while True:
            try:
                quantity = int(input("Please, Enter quantity to purchase: "))
                if quantity <= 0:
                    print("Quantity must be positive. So, Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                current_cost = products[product_id]["cost_price"]
                new_cost = input("Current cost price is NPR " + str(current_cost) + \
                                 ". Enter new price or press enter to keep same: ")
                if new_cost:
                    new_cost = float(new_cost)
                else:
                    new_cost = current_cost
                if new_cost <= 0:
                    print("Price must be positive. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        products[product_id]["quantity"] += quantity
        products[product_id]["cost_price"] = new_cost
        #adding the purchased product and update the price of the product inventory 
        products_purchased.append({
            "name": products[product_id]["name"],
            "brand": products[product_id]["brand"],
            "quantity": quantity,
            "cost_price": new_cost
        })
        
        total_amount += quantity * new_cost
        print("Added " + str(quantity) + " " + products[product_id]["name"] + " to purchase list.")
        
        while True:
            more_product = input("Do you want to purchase more items? (yes/no): ").lower()
            if more_product in ['yes', 'y', 'no', 'n']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if more_product in ['yes', 'y']:
            purchase_loop = True
        else:
            purchase_loop = False
    
    if products_purchased: # if the products_purchased is not empty
        save_products(products)
        create_purchase_invoice(products_purchased, supplier_name, total_amount)
    else:
        print("No products purchased.")

def sell_products(products):
    """
    Handles selling products to customers with a 'buy 3 get 1 free' offer, updating inventory and generating an invoice.
    
    Parameters:
        products (dict): A dictionary of products with IDs as keys and details as values (see read_products).
    
    Example:
        >>> products = {
                   1: {'name': 'Moisturizer', 'brand': 'Nivea', 'quantity': 10, 'cost_price': 500.0, 'origin': 'Germany'}
                 }
        >>> sell_products(products)
        Please, Enter customer name: Ram bahudur
        Please, Enter customer phone number: 1234567890
        Available Products:
        --------------------------------------------------------------------------------
        ID    Name                 Brand           Qty        Price (NPR)    Origin
        --------------------------------------------------------------------------------
        1     Moisturizer         Nivea           10         1000.0         Germany
        --------------------------------------------------------------------------------
        Enter product ID to sell (1 to finish): 1
        Enter quantity to sell (max 10): 3
        Dear John Doe, you get 1 free items with this purchase!
        Sold 3 Moisturizer with 1 free.
        Do you want to sell more items? (yes/no): no
        Shipping Information:
        Do you need shipping? (yes/no): yes
        Shipping cost: NPR 500 will be added to your total.
        [Generates and displays invoice, updates products dictionary]
    """
    print("\n------------------ Sell Products ----------------")
    while True:
        customer_name = input("Please, Enter the customer name: ")
        phone_number = input("Please, Enter the customer phone number: ")
        if customer_name == "" or phone_number == "":
            print("Please, Please the fill information \n ")
            continue
        try:
            int(phone_number)  # Check if phone_number can be converted to an integer
            if len(phone_number) != 10:  # Check if phone_number is exactly 10 digits
                print("Please, Enter the 10 digits phone number\n")
                continue
            break  # If both conditions are met, exit the loop
        except ValueError:
            print("Please, Enter the numeric value only in Phone number \n")
            continue
    products_sold = [] # creating the list to to store the sold product
    free_items = [] #creating the list to store the free product
    total_amount = 0
    shipping_cost = 0
    sell_loop = True

    while sell_loop == True:
        display_products(products)
        
        # Product ID input with validation
        while True: # infinite loop which will be exit by the break 
            try:
                product_id = int(input("\nEnter product ID to sell (1 to finish): "))
                if product_id not in products:
                    """gives the invaild when the product_id is not in the
                        products dictionary and contiune until the new id is not entry"""
                    print("Invalid product ID. Please enter a valid ID.")
                    continue
                break
            except ValueError: # handle if the non-numeric value is entry by the user 
                print("Invalid input. Please enter a number.")
        
        # Quantity input with validation
        while True: # infinite loop which will be exit by the break 
            try:
                max_available = products[product_id]["quantity"]
                quantity = int(input("Enter quantity to sell (max " + str(max_available) + "): "))
                
                if quantity <= 0:
                    print("Quantity must be positive. Please try again.")
                    continue
                
                free_qty = quantity // 3
                #"//": this is the floor division which will divide and rpovide the nearest round number
                total_quantity_to_deduct = quantity + free_qty
                
                if total_quantity_to_deduct > max_available:
                    
                    print("Only " + str(max_available) + " available. Cannot sell the " + \
                          str(quantity) + " quantity with " + str(free_qty) + " free.")
                    continue
                
                break
            except ValueError: # handle if the non-numeric value is entry by the user 
                print("Invalid input. Please enter a number.")
        
        # Process the sale
        products[product_id]["quantity"] -= total_quantity_to_deduct
        selling_price = products[product_id]['cost_price'] * 2
        #this will add the sold product into the sell product list
        products_sold.append({
            "name": products[product_id]["name"],
            "brand": products[product_id]["brand"],
            "quantity": quantity,
            "cost_price": products[product_id]["cost_price"],
            "free": free_qty
        })
        
        if free_qty > 0:
            free_items.append({
                "name": products[product_id]["name"],
                "brand": products[product_id]["brand"],
                "quantity": free_qty,
                "cost_price": products[product_id]["cost_price"]
            })
            print("Dear " + customer_name + ", you get " + str(free_qty) + \
                  " free items with this purchase!")
            
        # Ask if user wants to sell more
        while True:
            more = input("Do you want to sell more items? (yes/no): ").lower()
            if more in ['yes', 'y', 'no', 'n']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if more in ["yes", "y"]:
            sell_loop = True
        else:
             sell_loop = False
            
        # Ask about shipping at the beginning
        
        total_amount += quantity * selling_price # calculating the total price
        print("Sold " + str(quantity) + " " + products[product_id]['name'] + \
              " with " + str(free_qty) + " free.")
        
    # Ask about shipping at the beginning
    print("\nShipping Information:")
    while True:
        shipping = input("Do you need shipping? (yes/no): ").lower()
        if shipping in ['yes', 'y', 'no', 'n']:
            if shipping in ['yes', 'y']:
                shipping_cost = 500 #Fixed shipping cost is 500
                print("Shipping cost: NPR 500 will be added to your total.")
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    
    if products_sold: #only if the sold is no empty
        save_products(products)
        create_sale_invoice(products_sold, customer_name, phone_number, total_amount, free_items, shipping_cost)
    else:
        print("No products sold.")
