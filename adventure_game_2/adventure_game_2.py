import time

def game():
    answer = input("would you like to start the game? (y/n)")

    if answer.lower() == "y":
        print("Welcome to the game.")
        start = True
        inventory = []
    else:
        print("Okay. Maybe some other time then.")

    if start == True:
        print("Stranger: Hello traveler, I see you are new to this world.")
        print()
        print("Stranger: Well, welcome! This is the world of Adventoria. A Large and mysterious world.")
        print()
        print("Stranger: I can help you start out in this world if you would like.")



game()