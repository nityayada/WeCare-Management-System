from datetime import datetime
import random
from read import pad_string

def generate_bill_number(transaction_type):
    """
    Generates a unique bill number using timestamp and random number.
    
    Parameters:
        transaction_type (str): The type of transaction ('PURCHASE' or 'SALE').
    
    Returns:
        str: A bill number in the format 'TYPE-YYYYMMDDHHMMSS-RRR'
        (e.g., 'PURCHASE-20250503123045-123').
    
    Example:
        >>> generate_bill_number("PURCHASE")
        'PURCHASE-20250503123045-123'
        >>> generate_bill_number("SALE")
        'SALE-20250503123045-134'
    """
    present_time = datetime.now()
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    second = str(datetime.now().second)
    timestamp = year + month + day + hour + minute + second 
    random_num = random.randint(1, 999)
    return transaction_type.upper() + "-" + timestamp + "-" + str(random_num)



def save_products(products):
    """
    Saves product details back to the product file.
    
    Parameters:
        products (dict): A dictionary of products with IDs as keys and details as values (see read_products).
    
    Raises:
        Exception: If there is an error writing to 'product_details.txt'.
    
    Example:
        >>> products = {
              1: {'name': 'Vitamin C Serum', 'brand': 'Garnier', 'quantity': 10,
                  'cost_price': 500.0, 'origin': 'France'}
               }
        >>> save_products(products)
        # Creates/updates 'product_details.txt' with:
        # Vitamin C Serum,Garnier,10,500.0,France
    """
    try:
        with open("product_details.txt", "w") as file:
            for product_id, details in products.items():
                file.write(details["name"] + "," + details["brand"] + "," + 
                          str(details["quantity"]) + "," + str(details["cost_price"]) + 
                          "," + details["origin"] + "\n")
    except Exception as e:
        print("Error saving product file: " + str(e))

def create_purchase_invoice(products_purchased, supplier_name, total_amount):
    """
    Creates and displays a purchase invoice, saving it to a file.
    
    Parameters:
        products_purchased (list): A list of dictionaries, each containing:
            - 'name' (str): Product name.
            - 'brand' (str): Product brand.
            - 'quantity' (int): Purchased quantity.
            - 'cost_price' (float): Cost price per unit.
        supplier_name (str): The name of the supplier.
        total_amount (float): The total cost of the purchase.
   
    Raises:
        Exception: If there is an error writing the invoice file.
    
    Example:
        >>> products_purchased = [
             {'name': 'Vitamin C Serum', 'brand': 'Granier', 'quantity': 10,
                'cost_price': 500.0}
                ]
        >>> create_purchase_invoice(products_purchased, "Global Suppliers", 5000.0)
        ================================================================================
                        PURCHASE INVOICE DISPLAY
        ================================================================================
                WeCare Shop Purchase Invoice
            Kamalpokhari, Kathmandu | Phone No: 9811190255
        ================================================================================
        Supplier: Global Suppliers
        Invoice No: PURCHASE-20250503123045-123
        Date: 2025-05-03 12:30:45
        --------------------------------------------------------------------------------
        Product              Brand           Qty        Unit Price     Total
        --------------------------------------------------------------------------------
        Vitamin C Serum      Granier         10         500.0          5000.0
        --------------------------------------------------------------------------------
        Total Amount: NPR 5000.0
        Purchase invoice saved to: PURCHASE-20250503123045-123.txt
    """
    
    bill_number = generate_bill_number("PURCHASE")
    filename = bill_number + ".txt"
    
    try:
        # Create invoice content
        invoice_lines = []
        """Creating the invoice_lines list to put the all the details which should save in the
                file and display in the termianl """
        invoice_lines.append("\t\t\t\t WeCare Shop Purchase Invoice")
        invoice_lines.append("\t\t\t Kamalpokhari, Kathmandu | Phone No: 9811190255")
        invoice_lines.append("="*80)
        invoice_lines.append("Supplier: " + supplier_name)
        invoice_lines.append("Invoice No: " + bill_number)
        invoice_lines.append("Date: " + str(datetime.now()))
        invoice_lines.append("-" * 80)
        header = pad_string("Product", 20) + pad_string("Brand", 15) + \
                 pad_string("Qty", 10) + pad_string("Unit Price", 15) + pad_string("Total", 15)
        invoice_lines.append(header)
        invoice_lines.append("-" * 80)
        
        for product in products_purchased:
            line = pad_string(product["name"], 20) + pad_string(product["brand"], 15) + \
                   pad_string(str(product["quantity"]), 10) + \
                   pad_string(str(product["cost_price"]), 15) + \
                   pad_string(str(product["quantity"] * product["cost_price"]), 15)
            invoice_lines.append(line)
        
        invoice_lines.append("-" * 80)
        invoice_lines.append("Total Amount: NPR " +  str(total_amount))
        
        # Save to file
        with open(filename, "w") as file:
            file.write("\n".join(invoice_lines))
            #this will concatenate list into the single string with the new lines
        
        # Display on terminal
        print("\n" + "="*80)
        print("\t\t\t\t PURCHASE INVOICE DISPLAY")
        print("="*80)
        for line in invoice_lines:
            print(line)
        print("\nPurchase invoice saved to: " + filename)
        
    except Exception as e:
        print("Error creating purchase invoice: " + str(e))

def create_sale_invoice(products_sold, customer_name, phone_number, total_amount, free_items, shipping_cost):
    """
    Creates and displays a sales invoice, saving it to a file.
    
    Parameters:
        products_sold (list): A list of dictionaries, each containing:
            - 'name' (str): Product name.
            - 'brand' (str): Product brand.
            - 'quantity' (int): Sold quantity.
            - 'cost_price' (float): Cost price per unit.
            - 'free' (int): Number of free items (optional).
        customer_name (str): The name of the customer.
        phone_number (str): The customer's phone number.
        total_amount (float): The total cost of sold items (before shipping).
        free_items (list): A list of dictionaries for free items, each containing:
            - 'name' (str): Product name.
            - 'brand' (str): Product brand.
            - 'quantity' (int): Free quantity.
            - 'cost_price' (float): Cost price.
        shipping_cost (float): The cost of shipping (0 if no shipping).
   
    Raises:
        Exception: If there is an error writing the invoice file.
    
    Example:
        >>> products_sold = [
             {'name': 'Vitamin C Serum', 'brand': 'Grainer', 'quantity': 3,
             'cost_price': 500.0, 'free': 1}
              ]
        >>> free_items = [
             {'name': 'Moisturizer', 'brand': 'Nivea', 'quantity': 1,
          'cost_price': 500.0}
         ]
        >>> create_sale_invoice(products_sold, "Ram Prasad", "982332729", 3000.0, free_items, 500.0)
        ================================================================================
                        SALES INVOICE DISPLAY
        ================================================================================
                WeCare Shop Sales Invoice
            Kamalpokhari, Kathmandu | Phone No: 9811190255
        ================================================================================
        Customer Details:
        --------------------------------------------------------------------------------
        Customer: Ram Prasad
        Contact: 982332729
        Invoice No: SALE-20250503123045-123
        Date: 2025-05-03 12:30:45
        --------------------------------------------------------------------------------
        Product              Brand           Qty        Free       Unit Price     Total
        --------------------------------------------------------------------------------
        Moisturizer          Granier           3          1          1000.0         3000.0
        Free Items:
        Moisturizer (Granier) - 1 free
        --------------------------------------------------------------------------------
        Subtotal Amount: NPR 3000.0
        Shipping Cost: NPR 500.0
        Total Amount: NPR 3500.0
        Sales invoice saved to: SALE-20250503123045-123.txt
        
    """
    
    bill_number = generate_bill_number("SALE")
    filename = bill_number + ".txt"
    
    try:
        # Create invoice content
        invoice_lines = []
        """Creating the invoice_lines which include the all which should to displayed """
        invoice_lines.append("\t\t\t\tWeCare Shop Sales Invoice")
        invoice_lines.append("\t\t\tKamalpokhari, Kathmandu | Phone No: 9811190255")
        invoice_lines.append("="*80)
        invoice_lines.append("Customer Details:")
        invoice_lines.append("-"*80)
        invoice_lines.append("Customer: " + customer_name)
        invoice_lines.append("Contact: " + phone_number)
        invoice_lines.append("Invoice No: " + bill_number)
        invoice_lines.append("Date: " + str(datetime.now()))
        invoice_lines.append("-"*80)
        
        header = pad_string("Product", 20) + pad_string("Brand", 15) + \
                 pad_string("Qty", 10) + pad_string("Free", 10) + \
                 pad_string("Unit Price", 15) + pad_string("Total", 15)
        invoice_lines.append(header)
        invoice_lines.append("-"*80)
        
        for product in products_sold:
            selling_price = product["cost_price"] * 2
            line = pad_string(product["name"], 20) + pad_string(product["brand"], 15) + \
                   pad_string(product["quantity"], 10) + \
                   pad_string(product.get("free", 0), 10) + \
                   pad_string(str(selling_price), 15) + \
                   pad_string(str(product["quantity"] * selling_price), 15)
            invoice_lines.append(line)
        
        if free_items:# only proceed when the free_items is non empty 
            invoice_lines.append("\nFree Items:")
            for item in free_items:
                invoice_lines.append(item['name'] + " (" + item['brand'] + ") - " + \
                                     str(item['quantity']) + " free")
        
        invoice_lines.append("-"*80)
        invoice_lines.append("Subtotal Amount: NPR " + str(total_amount))
        if shipping_cost > 0:
            invoice_lines.append("Shipping Cost: NPR " + str(shipping_cost))
        invoice_lines.append("Total Amount: NPR " + str(total_amount + shipping_cost))
        
        
        # Save to file
        with open(filename, "w") as file:
            file.write("\n".join(invoice_lines))
        
        # Display on terminal
        print("\n" + "="*80)
        print("\t\t\t\t SALES INVOICE DISPLAY")
        print("="*80)
        for line in invoice_lines:
            print(line)
        print("\nSales invoice saved to: " + filename)
        
    except Exception as e:
        print("Error creating sales invoice: " + str(e))
