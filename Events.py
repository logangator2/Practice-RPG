
import random
import math
import Character

def battle(player_team, enemy_list):
    """
    Runs main battle simulation for any encounter. 
    Effects:
        Stats for characters change depending on outcome of battle.
    """
    check = 1
    n_enemies = len(enemy_list)
    og_enemies = []

    for e in enemy_list:
        og_enemies.append(e)

    if n_enemies == 1:
        print("Oh no! {} has appeared!".format(enemy_list[0].name))
    else:
        print("Oh no! Enemies have appeared!")

    # main battle while loop
    while check != 0:
        # check if all enemies have been defeated
        if len(enemy_list) == 0:
            print("You win! All enemies have been defeated.")
            value = 0

            # calc experience
            for e in og_enemies:
                value += e.calc_experience(player_team)
            value = math.ceil(value / len(player_team))

            # deal experience
            for p in player_team:
                p.gain_xp(value)
            break

        # display enemies
        for e in enemy_list:
            print("{},".format(e.name), "HP = {}".format(e.c_health))
            
        # request user input
        for p in player_team:
            p_in = input("What would you like {} to do? ".format(p.name))
            check = battle_command_checker(p_in.lower(), p, enemy_list)

        # FIXME: All code in this function below this comment needs to be changed when there len(player_team) > 1
        tmp_player = player_team[0]

        # have enemies attack if player entered in valid input
        if check == 3:
            for e in enemy_list:
                e.normal_attack(tmp_player) # ADD: add random moves for diff enemies
                if tmp_player.knockout:
                    print("You blacked out!") # FIXME: change to 'your team' later on - could check w/ if statement
                    return
                else:
                    print("{} has {} health. \n".format(tmp_player.name, tmp_player.c_health))
    return

def battle_command_checker(command, player, enemy_list):
    """
    Checks that player input is valid and executes command if so.
    Args:
        command: input from player
        player: character that user chose to execute command with
        enemy_list: list of enemies
    Effects:
        If player input is valid, executes command
    Returns:
        0 = Quit: If the player chose to quit, it quits the program
        1 = Help: If the player chose to display help, quit, or entered an invalid command, the game continues
        2 = All Clear: If all enemies have been defeated, sends 'all enemies defeated' signal to main
        3 = Valid Command: If player's action was completely valid and not help or quit
    """
    if len(enemy_list) == 0:
        return 2

    elif (command == "help") or (command == "h"):
        print("You may enter in any of these commands: fight, defend, status, or run") # FIXME: Update as necessary - items next
        print("You may use the first letter of each command instead.")
        return 1

    elif (command == "defend") or (command == "d"):
        print()
        player.defend()
        print()
        return 3

    # secret testing function
    elif (command == "ult"):
        player.c_health = 99999
        print("\nult enabled")
        return 1

    # display player status
    elif (command == "status") or (command == "s"):
        player.information()
        return 1

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

    elif (command == "run") or (command == "r"):
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
        slime = Character.Enemy("Slime {}".format(n + 1), 1, 0, 10, 0, "weak")
        enemy_list.append(slime)
    return enemy_list        

def event_picker(player_team):
    """
    Randomly picks an event 
    Args:
        player_team: list of player Character objects
    Effects:
        calls one of the specified events events
    """

    # FIXME: May want to just return a randomized selection of possible events so events aren't repeated

    rn = random.randint(1, 6)

    if rn == 1:
        slime_event(player_team)
    elif rn == 2:
        baby_event(player_team)
    elif rn == 3:
        print("\nYou have stumbled into a forgiving god's terrain.\n")
        for p in player_team:
            value = math.ceil(0.15 * p.health)
            p.healing(value)
    elif rn == 4:
        print("\n{} has fallen in a hole.\n".format(player_team[0]))
        player_team[0].damage(5)
    elif rn == 5:
        print("\nYou have a pleasant stroll along the road. The road is quiet.")
    elif rn == 6:
        g = random.randint(1, 100)
        player_team[0].gold += g
        print("\nYou found {} gold on the road!".format(g))
    
    # Ideas
        # gain an ally
        # arrive in a town
        # goblins attack
        # bandits
        # find chest w/ items
        # two groups are fighting and you have to choose between the two
        # troll asks you a riddle and if you don't know the answer you fight

def baby_event(player_team):
    """
    Runs the baby animal event
    Args:
        player_team: list of player Character objs
    """
    enemy_list = []
    check = True
    while (check):
        answer = (input("\nYou see a hurt baby animal on the road. Will you try and help it? Y/N ")).lower()
        if (answer == "yes") or (answer == "y"):
            print("\nThe animal was crying for its mother! The beast appears to defend its young.")
            enemy_list.append(Character.Enemy("Momma Bear", 1, 0, 20, 0, "average"))
            battle(player_team, enemy_list)
            check = False
            break
        elif (answer == "no") or (answer == "n"):
            print("\nYou leave the animal to die. You're a terrible person.")
            check = False
            break
        else:
            print("\nInvalid command! Try again.")
    return

def slime_event(player_team):
    """
    Runs slime event
    Args:
        player_team: list of player Character objects
    """

    enemy_list = slime_generator() # generate slime enemies
    battle(player_team, enemy_list)
    return
