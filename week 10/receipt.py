import csv
from datetime import datetime



KEY_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2



products_list = {}
amount_list = []
subtotal_list = []
tax_rate = 0.06025



def main():
    try:
        get_products("products.csv", KEY_INDEX)
        print("------------------------------------")
        print("GrocersGo")
        print("------------------------------------")
        print()
        print()
        customer_request()
        print()
        totals()
        print()
        current_date()

    except FileNotFoundError as file_not_found_err:
        print("Sorry, the specified file was not found")
        print("file_not_found_error")

    except PermissionError as perm_err:
        print(f"Error: cannot read from products.csv/request.csv because you don't have permission.")
        print("perm_err")

    except KeyError as key_err:
        print("Sorry, KeyError")
        print(type(key_err).__name__, key_err)



def get_products(file, key_index_): #This is my "read dictionary" function from the milestone. I renamed it.
    with open(file, "rt") as products:
        reader = csv.reader(products)
        next(reader)

        for line in reader:
            key = line[key_index_]
            products_list[key] = line
            products_list[key].pop(0)

    return products_list




def customer_request():
    with open("request.csv", "rt") as request:
        reader = csv.reader(request)
        next(reader)
        
        for line in reader:
            key = line[0]
            amount = line[1]
            requested_groceries = list(products_list[key])

            # print(requested_groceries)
            print(f"{requested_groceries[0].upper()}: {amount} At ${requested_groceries[1]} Each.")
            print()
    return request




def totals():
    with open("request.csv", "rt") as request:
        reader = csv.reader(request)
        next(reader)
        
        for line in reader:
            amount = int(line[1])
            amount_list.append(amount)

    total_items = (sum(amount_list))

    print("------------------------------------")
    print(f"Requested Items: {total_items}")


    with open("request.csv", "rt") as request:
        reader = csv.reader(request)
        next(reader)

        for line in reader:
            key = line[0]
            amount = float(line[1])
            requested_groceries = list(products_list[key])
            subtotal = amount * float(requested_groceries[1])
            subtotal_list.append(subtotal)
            final_subtotal = sum(subtotal_list)
            tax = final_subtotal * tax_rate
            final_total = tax + final_subtotal

        print(f"Subtotal: {final_subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print("------------------------------------")
        print(f"Total: {final_total:.2f}")
        print("------------------------------------")
        print("Thank you for shipping with GrocersGo. \nHave a fantastic day!")
        print("------------------------------------")



def current_date():
    current_time = datetime.now()
    print(f"{current_time:%c}")
    


if "__name__" == "__main__":
    main()