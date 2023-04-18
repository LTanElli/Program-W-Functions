import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list():
    for element in compound_list:
        print(element)
    print()
    

def sort_oldest_to_youngest(students_list):
    get_birthdate = lambda student: student[BIRTHDATE_INDEX]

    st = sorted(students_list, key = get_birthdate)

    return st
    pass

def sort_by_given_name(students_list):
    get_given_name = lambda student: student[GIVEN_NAME_INDEX]

    sorted_list = sorted(students_list, key = get_given_name)
    
    return sorted_list

def sort_by_month(students_list):
    get_birthdate = lambda student: student[BIRTHDATE_INDEX]

    sorted_list = sorted(students_list, key = get_birthdate)

    return sorted_list

    #     def extract_month_and_day(student):
    #         birthdate_string = student[BIRTHDATE_INDEX]
    #         month_and_day = birthdate_string[5:]
    #         return month_and_day
        
    # sorted_list = sorted(students_list, key = extract_month_and_day)

    # return sorted_list

def main():
    try:
        students_list = read_compound_list("pupils.csv")

        sorted_list1 = sort_oldest_to_youngest(students_list)
        print("From Oldest to Youngest:")
        print_list(sorted_list1)
        print()

        sorted_list2 = sort_by_given_name(students_list)
        print("From Given Name:")
        print()

        sorted_list3 = sort_by_month(students_list)
        print("From Birth Month:")
        print()

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep="")

    pass

if "__name__" == "__main__":
    main()
