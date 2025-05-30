def read_products():
    """
    Reads product details from a file and returns a dictionary of products.
    
   
    Returns:
        dict: A dictionary with product IDs as keys and details as values. Each product entry includes:
            - 'name' (str): The name of the product.
            - 'brand' (str): The brand of the product.
            - 'quantity' (int): The quantity available.
            - 'cost_price' (float): The cost price of the product.
            - 'origin' (str): The country of origin.
    
    Raises:
        FileNotFoundError: If 'product_details.txt' is not found.
        ValueError: If the file contains invalid data (e.g., non-numeric quantity or price).
    
    Example:
        >>> read_products()
        {
            1: {'name': 'Vitamin C Serum', 'brand': 'Garnier', 'quantity': 10, 'cost_price': 500.0, 'origin': 'France'},
            2: {'name': 'Sunscreen', 'brand': 'Lakme', 'quantity': 20, 'cost_price': 300.0, 'origin': 'India'}
        }
    """
    products = {}
    try:
        with open("product_details.txt", "r") as file:
            lines = file.readlines()
            product_id = 1
            for line in lines:
                line = line.replace("\n","").split(",")
                if len(line) >= 5:  # Ensure all required fields are present
                    products[product_id] = {
                        "name": line[0],
                        "brand": line[1],
                        "quantity": int(line[2]),
                        "cost_price": float(line[3]),
                        "origin": line[4]
                    }   
                    product_id += 1
    except FileNotFoundError:
        print("Error: Product file not found. Starting with empty inventory.")
    except Exception as e:
        print("Error reading product file: " + str(e))
    return products

def pad_string(text, length):
    """
    Pads a string with spaces to a specified length.
    
    Parameters:
        text (str or any): The text to pad (converted to string if not already).
        length (int): The desired length of the padded string.
    
    Returns:
        str: The padded string, with spaces added to reach the specified length.
    
    Example:
        >>> pad_string("ID", 5)
        'ID   '
        >>> pad_string(123, 6)
        '123   '
    """
    text = str(text)
    if len(text) >= length:
        return text
    return text + " " * (length - len(text))



