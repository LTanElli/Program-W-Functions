import csv
from datetime import datetime

KEY_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

request = {}
products_list = {}
amount_list = []
subtotal_list = []
tax_rate = 0.06025

def main():
    products_dict = read_dictionary()
    print(products_list)
    with open("request.csv", "rt") as req:
        reader = csv.reader(req)
    next(reader)
    # try:
    #     get_products("products.csv", KEY_INDEX)
    # pass
    try:
        get_products("products.csv", KEY_INDEX)

        print("Inkom Emporium")
        process_request()
        totals()
        date()

    except FileNotFoundError as file_not_found_err:
        print("Sorry, the specified file was not found")
        print("file_not_found_error")

    except PermissionError as perm_err:
        print(f"Error: cannot read from products.csv/request.csv because you don't have permission.")
        print("perm_err")

    except KeyError as key_err:
        print("Sorry, KeyError")
        print(type(key_err).__name__, key_err)

    


def get_products(products, key_column_index):
    with open("products.csv", "rt") as pro:
        reader = csv.reader(pro)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            products_list[key] = row
            products_list[key].pop(0)
    return products_list

def process_request():
    with open("request.csv", "rt") as req:
        reader = csv.reader(req)
        next(reader)
        # print(" ")
        for line in reader:
            key = line[0]
            amount = line[1]
            names = list(products_list[key])
            print(f"{names[0]}: {amount} @ {names[1]}")j
    return request

def read_dictionary(): 
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    pass
def totals():
    with open("request.csv", "rt") as req:
        reader = csv.reader(req)
        next(reader)
        # print(" ")
        for line in reader:
            amount = int(line[1])
            amount_list.append(amount)
    total_items = (sum(amount_list))
    print(f"Requested Items: {total_items}")

    with open("products.csv", "rt") as pro:
        reader = csv.reader(pro)
        next(reader)
        for line in reader:
            key = line[0]
            amount = float(line[1])
            names = list(products_list[key])
            subtotal = amount * float(names[1])
            subtotal_list.append(subtotal)
            final_subtotal = sum(subtotal_list)
            tax = final_subtotal * tax_rate
            total = tax + final_subtotal
        print(f"Subtotal: {final_subtotal}")
        print(f"Sales tax: {tax:.2f}")
        print(f"Total: {total:.2f}")
        print(" ")
        print("Thank you for shipping with Inkom Emporium")

def date():
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%c}")
    

if "__name__" == "__main__":
    main()