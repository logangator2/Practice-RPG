
import Character
import Enemy
import random

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

def command_checker(command, player, enemy_list):
    """
    Checks that player input is valid and executes command if so.
    Args:
        command: input from player
        enemy_list: list of enemies
    Effects:
        If player input is valid, 
    Returns:
        0: If the player chose to quit, it quits the program
        1: If the player chose to display help, quit, or entered an invalid command, the game continues
        2: If all enemies have been defeated, sends 'all clear' signal to main
    """
    if len(enemy_list) == 0:
        return 2

    if (command == "Help") or (command == "help"):
        print("You may enter in any of these commands: fight, quit") # FIXME: Update when more features added
        return 1

    elif (command == "Fight") or (command == "fight"):
        for e in enemy_list:
            # check if enemy is still alive, else remove from list
            if e.c_health == 0:
                enemy_list.remove(e) # FIXME: not removing correctly, removes next enemy temporarily after current enemy dies
                continue
            else:
                print("{},".format(e.name), "HP = {}".format(e.c_health))
        target = input("Which enemy would you like to attack? ")

        # check for valid target
        for e in enemy_list:
            if e.name == target:
                player.normal_attack(e)
                return 1
        print("Invalid target! Try again.")
        return 1

    elif (command == "Quit") or (command == "quit"): # FIXME: Once Overworld is added, change quit to run 
        return 0

    else:
        print("Invalid command! Please retry.")
        return 1

def main():
    check = 1
    still_enemies = True
    enemy_list = slime_generator() # generate slime enemies

    # create player character
    p_name = input("Enter your name: ")
    player = Character.Character(p_name, 20)

    print()
    print("Welcome, {}. You have {} health.".format(player.name, player.c_health))
    print()
    n_enemies = len(enemy_list)

    if n_enemies == 1:
        print("Oh no! A slime has appeared!")
    else:
        print("Oh no! {} slimes have invaded!".format(n_enemies))

    # main game while loop
    while check != 0:
        # check if all enemies have been defeated
        if check == 2:
            print("All enemies have been defeated.")
            return
        p_in = input("What would you like to do? ")
        check = command_checker(p_in, player, enemy_list)




if __name__ == '__main__':
    main()