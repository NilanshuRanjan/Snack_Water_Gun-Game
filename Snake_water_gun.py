import random


def snake_water_gun():
    l = ["s","g","w"]
    user_points = 0
    comp_points = 0
    n = int(input("\nenter max points: "))
    while True:
        user = input("\nenter s for snake w for water and g for gun: ")
        comp_input = random.choice(l)

        if comp_input == "s":
            print("computer input is Snake")
        if comp_input == "w":
            print("computer input is Water")
        if comp_input == "g":
            print("computer input is Gun")

        if user == "s":
            if comp_input == "w":
                user_points += 1
            elif comp_input == "g":
                comp_points += 1
        elif user == "w":
            if comp_input == "g":
                user_points += 1
            elif comp_input == "s":
                comp_points += 1
        elif user == "g":
            if comp_input == "s":
                user_points += 1
            elif comp_input == "w":
                comp_points += 1

        print("computer score ==", comp_points, "\nYour score == ", user_points)

        if comp_points == n:
            print("computer wins")
            break
        elif user_points == n:
            print("You win")
            break
    ch = input("\nwanna play again if yes then enter Y: ")
    if ch in "Yy":
        snake_water_gun()

snake_water_gun()
