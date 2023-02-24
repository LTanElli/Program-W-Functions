import random

def main():
    """
    Has no parameters
Creates a list named numbers like this:
numbers = [16.2, 75.1, 52.3]
Prints the numbers list
Calls the append_random_numbers function with only one argument to add one number to numbers
Prints the numbers list
Calls the append_random_numbers function again with two arguments to add three numbers to numbers
Prints the numbers list
    """
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers: {numbers}")

    append_random_numbers(numbers)
    print(f"numbers: {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers: {numbers}")


def append_random_numbers(numbers_list, quantity = 1):
    """
    Has two parameters: a list named numbers_list and an integer named quantity. 
    The parameter quantity has a default value of 1
    Computes quantity pseudo random numbers by calling the random.uniform function.
    Rounds the quantity pseudo random numbers to one digit after the decimal.
    Appends the quantity pseudo random numbers onto the end of the numbers_list.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 50)
        rounded_numbers = round(random_number, 1)
        numbers_list.append(rounded_numbers)

if __name__ == "__main__":
    main()
    

