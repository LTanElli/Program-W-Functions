#nouns: item, cart, description, price

def load():
    pass

def save():
    pass

def add_item(items, prices):
    item = input("enter item: ")
    price = input("enter price: ")
    items.append(item)
    prices.append(price)
    

def display(items, prices):
    """displays the contents of the items with prices"""
    print("items      |     prices")
    print("-----------------------")
    for i in range(len(items)):
        print(f"{items[i]}  |  {prices[i]}")
    

def remove():
    pass



def main():
    items = []
    prices = []
    pass



main()