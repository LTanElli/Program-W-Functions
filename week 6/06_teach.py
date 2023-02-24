"""
I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.
"""

print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
print()
print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")

question1 = input("1. I feel that I am a person of worth, at least on an equal plane with others. \nEnter D, d, a, or A: ")
print()
question2 = input("2. I feel that I have a number of good qualities. \nEnter D, d, a, or A: ")
print()
question3 = input("3. All in all, I am inclined to feel that I am a failure. \nEnter D, d, a, or A: ")
print()
question4 = input("4. I am able to do things as well as most other people. \nEnter D, d, a, or A: ")
print()
question5 = input("5. I feel I do not have much to be proud of. \nEnter D, d, a, or A: ")
print()
question6 = input("6. I take a positive attitude toward myself. \nEnter D, d, a, or A: ")
print()
question7 = input("7. On the whole, I am satisfied with myself. \nEnter D, d, a, or A: ")
print()
question8 = input("8. I wish I could have more respect for myself. \nEnter D, d, a, or A: ")
print()
question9 = input("9. I certainly feel useless at times. \nEnter D, d, a, or A: ")
print()
question10 = input("10. At times I think I am no good at all. \nEnter D, d, a, or A: ")
print()

def main():
    print(f"Your score is {total_values()}.")
    print("A score below 15 may indicate problematic low self-esteem.")
    pass

def positive_values():
    # question numbers 1, 2, 4, 6, 7. Score 0-3
    if question1 == "D":
        question1 = 0
    elif question1 == "d":
        question1 = 1
    elif question1 == "a":
        question1 = 2
    else:
        question1 == "A"
        question1 = 3

    if question2 == "D":
        question2 = 0
    elif question2 == "d":
        question2 = 1
    elif question2 == "a":
        question2 = 2
    else:
        question2 == "A"
        question2 = 3

    if question4 == "D":
        question4 = 0
    elif question4 == "d":
        question4 = 1
    elif question4 == "a":
        question4 = 2
    else:
        question4 == "A"
        question4 = 3

    if question6 == "D":
        question6 = 0
    elif question6 == "d":
        question6 = 1
    elif question6 == "a":
        question6 = 2
    else:
        question6 == "A"
        question6 = 3

    if question7 == "D":
        question7 = 0
    elif question7 == "d":
        question7 = 1
    elif question7 == "a":
        question7 = 2
    else:
        question7 == "A"
        question7 = 3

    print(f"{question1}, {question2}, {question4}, {question6}, {question7}")
    positive_total = question1 + question2 + question4 + question6 + question7
    return positive_total

def negative_values():
    # qestion numbers 3, 5, 8, 9, 10. Score 3-0
    if question3 == "D":
        question3 = 3
    elif question3 == "d":
        question3 = 2
    elif question3 == "a":
        question3 = 1
    else:
        question3 == "A"
        question3 = 0

    if question5 == "D":
        question5 = 3
    elif question5 == "d":
        question5 = 2
    elif question5 == "a":
        question5 = 1
    else:
        question5 == "A"
        question5 = 0
    
    if question8 == "D":
        question8 = 3
    elif question8 == "d":
        question8 = 2
    elif question8 == "a":
        question8 = 1
    else:
        question8 == "A"
        question8 = 0

    if question9 == "D":
        question9 = 3
    elif question9 == "d":
        question9 = 2
    elif question9 == "a":
        question9 = 1
    else:
        question9 == "A"
        question9 = 0

    if question10 == "D":
        question10 = 3
    elif question10 == "d":
        question10 = 2
    elif question10 == "a":
        question10 = 1
    else:
        question10 == "A"
        question10 = 0

    print(f"{question3}, {question5}, {question8}, {question9}, {question10}")
    negative_total = question3 + question5 + question8 + question9 + question10
    return negative_total

def total_values():
    total = positive_values() + negative_values()
    print(f"{total}")
    

main()