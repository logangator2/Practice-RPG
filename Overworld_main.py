
import random

import Character
import Events

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
            player = Character.Character(p_name, 1, 0, 20, 0)
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
            check = False
            break
            
        # check if players are still alive
        all_dead = True
        for p in player_team:
            if p.dead != True:
                all_dead = False
        if all_dead:
            print("\nYour adventure is over.\n")
            check = False
            break
            
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
