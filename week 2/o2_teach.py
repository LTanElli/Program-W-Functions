from datetime import datetime

subtotal = float(input("Please enter the subtotal: "))
sales_tax = float(input("Please enter the sales tax: "))

dt = datetime.now()

day = dt.weekday()

print(day)

if subtotal > 50:
    final_price = subtotal + sales_tax
    discount_amount = final_price * 0.10
    discount_price = final_price - discount_amount
    print(f"The discount amount is {discount_amount}")
    print(f"The final price is {final_price:.2f}, the discounted price is {discount_price:.2f}")

elif day == 1 or day == 2:
    final_price = subtotal + sales_tax
    discount_amount = final_price * 0.10
    discount_price = final_price - discount_amount
    print(f"The discount amount is {discount_amount}")
    print(f"The final price is {final_price:.2f}, the discounted price is {discount_price:.2f}")

else:
    final_price = subtotal + sales_tax
    print(f"The final price is {final_price:.2f}")