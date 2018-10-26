
import random
import Character
import Enemy

def battle_command_checker(command, player, enemy_list):
    """
    Checks that player input is valid and executes command if so.
    Args:
        command: input from player
        enemy_list: list of enemies
    Effects:
        If player input is valid, executes command
    Returns:
        0: If the player chose to quit, it quits the program
        1: If the player chose to display help, quit, or entered an invalid command, the game continues
        2: If all enemies have been defeated, sends 'all enemies defeated' signal to main
        3: If player's action was completely valid and not help or quit
    """
    if len(enemy_list) == 0:
        return 2

    elif (command == "help") or (command == "h"):
        print("You may enter in any of these commands: fight, defend, or run") # FIXME: Update as necessary
        print("You may use the first letter of each command instead.")
        return 1

    # secret testing function
    elif (command == "ult"):
        player.c_health = 500
        return 1

    elif (command == "defend") or (command == "d"):
        print()
        player.defend()
        print()
        return 3

    elif (command == "fight") or (command == "f"):
        target = input("Which enemy would you like to attack? ")

        # check for valid target
        for e in enemy_list:
            if e.name.lower() == target.lower():
                print()
                player.normal_attack(e)
                print()
                if e.dead:
                    enemy_list.remove(e)
                return 3

        print("Invalid target! Try again.")
        return 1

    elif (command == "run") or (command == "r"): # FIXME: Once Overworld is added, add 'run' option
        print("You run!")
        return 0

    else:
        print("Invalid command! Please retry.")
        return 1

def slime_generator():
    """
    Generates a random number of slime enemies
    # NOTE: intended to scale to generating more types of enemies
    Returns:
        enemy_list: a list of enemy slimes
    """
    enemy_list = []
    n_slimes = random.randint(1, 5)

    for n in range(n_slimes):
        slime = Enemy.Enemy("Slime {}".format(n + 1), 10)
        enemy_list.append(slime)
    return enemy_list        

def slime_event(player):

    check = 1
    enemy_list = slime_generator() # generate slime enemies
    n_enemies = len(enemy_list)

    if n_enemies == 1:
        print("Oh no! A slime has appeared!")
    else:
        print("Oh no! {} slimes have invaded!".format(n_enemies))

    # main game while loop
    while check != 0:
        # check if all enemies have been defeated
        if len(enemy_list) == 0:
            print("You win! All enemies have been defeated.")
            break

        for e in enemy_list:
            print("{},".format(e.name), "HP = {}".format(e.c_health))
        # request user input
        p_in = input("What would you like to do? ")
        check = battle_command_checker(p_in.lower(), player, enemy_list)

        # have enemies attack if player entered in valid input
        if check == 3:
            for e in enemy_list:
                e.normal_attack(player) # FIXME: will want to change to random move with diff enemies
                if player.knockout:
                    print("You blacked out!") # FIXME: change to 'your team' later on
                    return
                else:
                    print("{} has {} health. \n".format(player.name, player.c_health))
    return