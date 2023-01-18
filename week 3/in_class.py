#functions format
def display_welcome():
    print("Welcome")

display_welcome()


#function rules
#1) should do one thing
#2) be able to describe it in one sentence
#3) don't use "and" or "or". call back to rule number one.
#4) must fit on the screen


# purpose of main? 
# can create a string of functions being called while calling only one function
def add_two(x):
    return x + 2

def add_three(x):
    answer = x + 3
    return answer

def main():
    answer = add_two(10)
    print(f"Answer equals {answer}")
    print(f"answer equals {add_three(10)}")

main()


