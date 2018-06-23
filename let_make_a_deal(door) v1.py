"""
class: lets make a deal

Methods:
display current status of the game - boolean Did you win the game? False = No, True = Yes, None = Game still in progress
ask user for input - boolean Did user enter a valid input? if so, it will update user choice and previous selection accordingly .
display a "zonk" - int returns the index of the zonk revealed?
ask if user would like to change input - boolean verifies if the function was suceussful.

Member variables:
User's choice - int
Door option - list of int
previous selection- int
winning door - int

"""
import random


class lets_make_a_deal():
    def __init__(self):
        self.users_choice = None
        self.door_options = [1, 2, 3]
        self.previous_selection = None
        self.winning_door = random.randint(0, len(self.door_options) - 1)

    def display_current_status(self):
        if self.users_choice is None:
            print("There are " + str(len(self.door_options)) + " doors and a door must be selected")
            return None
        else:
            print("There are " + str(len(self.door_options)) + " doors and the user has selected door #" + str(self.door_options[self.users_choice]))
            if self.previous_selection is None:
                print("Please ask the user if he would like to change his selection")
                return None
            else:
                if self.winning_door == self.users_choice:
                    print("YOU HAVE WON THE GAME!")
                    return True
                else:
                    print("You lost the game =(")
                    print("The door you selected was door #" + str(self.door_options[self.users_choice]))
                    if self.previous_selection == self.winning_door:
                        print("If did not change your door selection, you would have won =P!")
                print("The winning door was door #" + str(self.door_options[self.winning_door]))
                return False

    def ask_user_input(self):
        selection = int(input("Which door number would you like to select? (1-" + str(len(self.door_options)) + ")")) - 1
        if selection >= 0 and selection < len(self.door_options):
            if self.previous_selection is None and self.users_choice is not None:
                self.previous_selection = self.users_choice
            self.users_choice = selection
            return True
        return False

    def ask_user_to_change_option(self):
        answer = input("Would the user like to change his answer? (Y/N)")
        if answer.lower() == 'y':
            self.ask_user_input()
        else:
            self.previous_selection = self.users_choice
        return True

    def display_zonk(self):
        possible_zonks = list(self.door_options)
        del possible_zonks[self.users_choice]
        if self.winning_door != self.users_choice:
            if self.users_choice < self.winning_door:
                del possible_zonks[self.winning_door - 1]
            else:
                del possible_zonks[self.winning_door]

        zonk_index = random.randint(0, len(possible_zonks)-1)
        print("Door " + str(possible_zonks[zonk_index]) + " is a zonk ")
        return (zonk_index)


game = lets_make_a_deal()
game.display_current_status()
game.ask_user_input()
print("------")
game.display_zonk()
print("------")
game.ask_user_to_change_option()
print("------")
game.display_current_status()
