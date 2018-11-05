
import random
import math

import Character
import Events

def still_alive(player_team):
    """
    Checks if player team is still alive.
    Args:
        player_team: list of player objects
    Returns:
        True if players are still alive
        False if players are all dead
    """
    all_dead = True
    for p in player_team:
        if p.dead != True:
            all_dead = False
            return True

    if all_dead:
        print("\nYour adventure is over.\n")
        return False

def main():
    """
    Main game loop of the Practice RPG
    """
    
    # main loop checker
    check = True

    # loop to select whether to continue from old save
    while (check):
        cmd = input("Please select an option: 1: New Game, 2: Continue Game, 3: Quit. ")

        if cmd == "1":
            # create player character
            p_name = input("Enter your name: ")
            player = Character.Character(p_name, 1, 0, 20, 10)
            player_team = [player]

            # opening message
            print("\nWelcome, {}. You have {} health.".format(player.name, player.c_health))

            event_counter = 0
            check = False
            break

        if cmd == "2":
            # open file
            print("\n Welcome back!")
            break
        if cmd == "3":
            return
        else:
            print("\nInvalid command! Try again.")

    # set loop checker back to normal
    check = True

    # main game loop
    while (check):
        
        # check if enough events have occurred
        if event_counter == 10:
            print("\nYou've had quite an adventure!\n")
            check = False
            break
            
        # check if players are still alive
        check = still_alive(player_team)
        if check == False:
            break

        # check if players aren't all knocked out, if one is, heal
        all_ko = True
        for p in player_team:
            if p.knockout != True:
                all_ko = False
            else:
                print() # formatting
                p.healing(1)
                print("\n{} has awakened!".format(p.name))

        # if all players are knocked out, have them lose 15% of their average gold each
        lost_gold = 0
        if all_ko:
            for p in player_team:
                lost_gold += math.floor(0.15 * p.gold)
            for p in player_team:
                p.gold -= math.floor(lost_gold / len(player_team))
            print("\nYour adventurers wake up, but have lost {} gold.".format(lost_gold))
            
        # continue adventure
        else:
            print("\nYou are walking along a road.\n")
            # ask for player input
            command = input("What would you like to do? Type 'Help' for commands. ")
            command = command.lower()
                       
            # display possible commands
            if (command == "help") or (command == "h"):
                print("\nYou may enter in any of these commands: move, status, quit")
                print("You may use the first letter of each command instead.")
       
            # secret testing function
            elif (command == "ult"):
                for p in player_team:
                    p.c_health = 99999
                print("\nult enabled")

            # display player team status
            elif (command == "status") or (command == "s"):
                for p in player_team:
                    print("{}".format(p.information()))

            # trigger event
            elif (command == "move") or (command == "m"):
                print("\nYou move along the road.")
                Events.event_picker(player_team)
                event_counter += 1
                       
            # quit game
            elif(command == "quit") or (command == "q"):
                check = False
                break
            else:
                print("\nInvalid command! Please retry.")
    return


if __name__ == '__main__':
    main()
