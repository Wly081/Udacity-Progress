import time


import random


action_options = ["1", "2"]
item = []
possible_loot = ["sword", "dagger", "torch", "book", "ruby gem"]


def print_pause(item_to_print, time_to_wait):
    print(item_to_print)
    time.sleep(time_to_wait)


def valid_input(prompt):
    while True:
        choice = input(prompt)
        if choice in action_options:
            break
        else:
            print("I don't understand")
    return choice


def escaped():
    print_pause("You have escaped the cave!", 2)
    print_pause("You won!!!", 2)


def death():
    print_pause("The goblin caught you!", 2)
    print("You died! :( ")


def intro():
    print_pause("You find yourself standing in an open field," +
                "filled with grass and yellow wildflowers." +
                "Rumor has it that a wicked fairie is somewhere around here," +
                "and has been terrifying the nearby village.\n""...", 2)


def field():
    print_pause("1. knock on the door of the house.", 2)
    print_pause("2. to peer into the cave. ", 2)
    print("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2)")
    if choice == "1":
        house()
    elif choice == "2":
        cave()
    else:
        print("I don't understand")


def house():
    while True:
        print_pause("you knocked on the door but no one answered," +
                    "so you decided to enter the house", 2)
        print_pause("you have entered the house and suddenly," +
                    "a goblin jumps in front of you", 2)
        print_pause("What do you want to do?", 2)
        print_pause("1.Fight", 2)
        print_pause("2. Run", 2)
        goblin = valid_input("(Please enter 1 or 2)")
        if goblin == "1":
            if "sword" in item:
                print("You killed the goblin with the sword from the cave!")
                escaped()
                break
            else:
                print("you do not have a good weapon to kill this monster")
                death()
                break
        elif goblin == "2":
            print("The goblin runs faster than you!")
            death()
            break
        else:
            print("I don't understand")


def cave():
    loot = random.choice(possible_loot)
    print_pause("Lucky! you found a " + loot + " in a fancy chest", 2)
    item.append(loot)
    print_pause("There is nothing else here, returning to the field", 2)
    field()


def play_again():
    while True:
        print_pause("Do you want to play again?", 2)
        print_pause("1.Yes", 2)
        print_pause("2. No", 2)
        token = valid_input("(Please enter 1 or 2)")
        if token == "1":
            play_game()
        elif token == "2":
            print("Thanks for playing!!")
            break
        else:
            print("Sorry I don't understand")


def play_game():
    intro()
    field()
    play_again()


play_game()
