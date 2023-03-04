# Daniel Burton 1-27-2023
# Lab 1

# Exercise 1-2: Hello Word Typos
print("Hell0 Python Wor1d_!")
print("He11o-Python_W0rld!")

# Exercise 2-1: Simple Message
sleep = int(input("How many hours did you sleep last night? "))

if sleep < 6:
    tired = "You need a nap."
    print(tired)
elif sleep >= 6:
    hungry_tired = "You don't need a nap. Get to work."
    print(hungry_tired)

# Exercise 2-2: Simple Messages
dr_peppy = input("Does your fry's have dr pepper? ").lower()
if dr_peppy == "yes":
    kroger = "Fry's is the best!"
    print(kroger)
elif dr_peppy == "no":
    kroger = "Fry's is the worst!"
    print(kroger)
