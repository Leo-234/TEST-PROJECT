import random
inventory = []
def game_clear():
    return
def game_over():
    print("Game over. Do you want to play again?")
    choice = input("Type 'yes' to plau again or 'no' to quit: ")
    if choice.lower() == "yes":
        print("starting game: ")
        introduction()
    elif choice.lower() == "no":
        print("thank you for playing")
    else: 
        print("invalid choice, try again")
        game_over()

def river_path():
    print("You arrive at the river, you see a gun")
    print("Type 'gun' to pick up gun or 'leave' to leave: ")

    choice = input("will you pick it up or leave it?: ")
    if choice.lower() == "gun":
        if "gun" not in inventory:
            inventory.append ("gun")
            print("you pick up the gun")
        else:
            print("you already have a gun")
    elif choice.lower() == "leave":
        print("you leave the fun behind")
    else:
        print("Choose between given options: ")
        river_path()
    print("there is nothing else, you go to the cave: ")
    cave_path()

def cave_path():
    print("You enter the cave and see a sleeping dragon")
    print("Type 'shoot' to shoot it or 'run' to leave")

    choice = input("shoot or run?: ")

    if choice.lower() == "shoot":
        if "gun" in inventory:
            shoot_dragon()
        else: 
            print("You need a gun to shoot the dragon")
            cave_path()
    elif choice.lower() == "river":
        print("you rush back to the river")
        river_path()
    elif choice.lower() == "run":
        print("The dragon wakes up and eats you. Game Over:")
        game_over()
    else:
        print("Invalid choice: try again: ")
        cave_path()


def shoot_dragon():
    print("you aim your gun at the dragon")
    print("you shoot.")
    shots = random.randint(1,5)
    print("you shot", shots, "times")
    if shots >= 3:
        print("you fired at least 3 shots and killed the dragon. You won!")
        game_clear()
    else:
        print("You didn't have enough shots to kill the dragon. You Lose!")
        game_over()
def introduction():
    print("welcome to the adventure game")
    print("you are in a forest")
    print("type 'cave' to expolore the cave or 'river' to go to the river")

    choice = input("Which way will you go?: ")

    if choice.lower() == "cave":
        cave_path()
    elif choice.lower() == "river":
        river_path()
    else:
        print("choose one of the given paths: ")
        introduction()

introduction()