import csv as students

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    students_dict = read_dictionary(students, I_NUMBER_INDEX)
    
    number = input("Please enter your I-Number (xx-xxx-xxxx): ")
    number = number.replace("-", "")

    if not number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if number not in students_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students_dict[number]
                name = value[NAME_INDEX]

                # Print the student name.
                print(name)
    pass

def read_dictionary(students, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open("students.csv", "rt") as csv_file:
        reader = students.reader(csv_file)

        next(reader)

        for row_list in reader:
            keys = row_list[key_column_index]

            dictionary[keys] = row_list

    return dictionary


if __name__ == "__main__":
    main()


