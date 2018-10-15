
import Character
import random

def slime_generator():
    """
    Generates a random number of slime enemies
    Returns:
        enemy_list: a list of enemy slimes
    """
    enemy_list = []
    n_slimes = random.randint(1, 5)

    for n in range(n_slimes):
        slime = Character.Character("Slime {}".format(n + 1), 10)
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
        2: If the player has defeated all of the enemies
    """
    if (command == "Help") or (command == "help"):
        print("You may enter in any of these commands: fight, quit") # FIXME: Update when more features added
        return 1

    elif (command == "Fight") or (command == "fight"):
        for e in enemy_list:
            print(e.name)
        target = input("Which enemy would you like to attack? ")

        for e in enemy_list:
            if e.name == target:
                player.normal_attack(e)
                return 1
        print("Invalid target! Try again.")
        return 0

    elif (command == "Quit") or (command == "quit"):
        return 0

    else:
        print("Invalid command! Please retry.")
        return 1

def main():
    check = 1
    enemy_list = slime_generator()
    p_name = input("Enter your name: ")
    player = Character.Character(p_name, 20)

    print()
    print("Welcome, {}. You have {} health.".format(player.name, player.c_health))
    n_enemies = len(enemy_list)
    if n_enemies == 1:
        print("Oh no! A slime has appeared!")
    else:
        print("Oh no! {} slimes have invaded!".format(n_enemies))

    while check != 0:
        p_in = input("What would you like to do? ")
        check = command_checker(p_in, player, enemy_list)




if __name__ == '__main__':
    main()