<h1>WeCare-Management-System</h1>

<h2>Overview</h2>

<p>The WeCare Shop Management System is a Python-based console application designed to manage inventory, purchases, and sales for a skincare product shop. It reads product details from a file, supports restocking and selling operations, and generates detailed invoices for transactions. The system emphasizes user-friendly input validation and data persistence, making it efficient for small-scale retail management.</p>

<h3>Features</h3>
<ul>
<li>Inventory Management: Load and display product details (name, brand, quantity, cost price, origin) from product_details.txt.</li>
<li>Product Display: View available products with a 200% markup selling price.</li>
<li>Purchase Products: Restock inventory by purchasing products from suppliers, updating quantities and prices, and generating purchase invoices.</li>
<li>Sell Products: Sell products to customers with a "buy 3 get 1 free" offer, validate stock availability, and generate sales invoices with optional shipping costs (NPR 500).</li>
<li>Invoice Generation: Create and save detailed purchase and sales invoices with unique bill numbers (e.g., PURCHASE-20250503123045-123.txt).</li>
<li>Input Validation: Ensure valid numeric inputs for product IDs, quantities, prices, and 10-digit phone numbers.</li>
<li>Data Persistence: Save updated product details back to product_details.txt after transactions.</li>
<li>Error Handling: Robust handling for file operations, invalid inputs, and insufficient stock.</li>
</ul>

<h3>Project Structure</h3>
<ul>
<li>main.py: Entry point with the main menu and welcome message.</li>
<li>read.py: Reads product data and provides string padding for formatted output.</li>
<li>write.py: Handles invoice generation and saving product data.</li>
<li>operations.py: Manages product display, purchase, and sales operations.</li>
<li>product_details.txt: Stores product data (name, brand, quantity, cost price, origin).</li>
</ul>

<h3>How to Run</h3>
<ul>
<li>Ensure Python 3.x is installed.</li>
<li>Place all files (main.py, read.py, write.py, operations.py, product_details.txt) in the same directory.</li>
<li>Run main.py using a Python interpreter:
python main.py</li>
<li>Follow the console prompts to navigate the menu and perform operations.</li>
</ul>

<h3>Technologies Used</h3>
<ul>
<li>Python: Core programming language.</li>
<li>File I/O: For reading and writing product and invoice data.</li>
</ul>

<h3>Usage</h3>
<ul>
<li>Display Products: View available products with their selling prices (option 1).</li>
<li>Purchase Products: Restock inventory by entering supplier details, product IDs, quantities, and optional new prices (option 2).</li>
<li>Sell Products: Sell products to customers, apply free item offers, and specify shipping needs (option 3).</li>
<li>Exit: Close the system (option 4).</li>
<li>Invoices are saved as text files with unique bill numbers, and product data is updated in product_details.txt.</li>
</ul>

<h3>Future Enhancements</h3>
<ul>
<li>Add a GUI for improved user interaction.</li>
<li>Implement a database for scalable storage.</li>
<li>Support additional discounts or promotions.</li>
<li>Add reporting for sales and inventory trends.</li>
</ul>
