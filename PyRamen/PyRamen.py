from pathlib import Path
import csv

# Set the file path
menu_csv = Path("Resources/menu_data.csv")
sales_csv = Path("Resources/sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open (menu_csv, "r") as csvmenu:
    csvmenu = csv.reader(csvmenu)
    header = next(csvmenu)
    
    for row in csvmenu:
        menu.append(row)

# @TODO: Read in the sales data into the sales list
with open (sales_csv, "r") as csvsales:
    csvsales = csv.reader(csvsales)
    
    header2 = next(csvsales)
  
    for row in csvsales:
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

#  @TODO: Loop over every row in the sales list object

for row in sales:
    
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(row[3])
    menu_item = row[4]

     #@TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report.keys():
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,}

    # @TODO: For every row in our sales data, loop over the menu records to determine a match

    for record in menu:  
    # Item,Category,Description,Price,Cost
    # @TODO: Initialize menu data variables
        item = record[0]
        price = float(record[3])
        cost = float(record[4])

        # @TODO: Calculate profit of each item in the menu data
        """ If the sales_item in sales is equal to the item in menu, capture the quantity from the sales data and the price and cost from the menu data to calculate the profit for each item"""
        
        profit = (price - cost) * quantity 

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item:
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit          
            #print(menu_item)    
        else:
            print(f"{menu_item} does not equal {item}! NO MATCH!")
            pass 

    # @TODO: Increment the row counter by 1
    row_count += 1
    pass 

# @TODO: Print total number of records in sales data
print(sales)
# @TODO: Write out report to a text file (won't appear on the command line output)
with open ("report.csv", "w") as csv_report:
    for key, value in report.items():
        line= f"{key}, {value} \ in"
        csv_report.write(line)