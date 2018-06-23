"""
class: lets make a deal

Methods:
boolean, display current status of the game - If the game ends right now, did you win the game? False = No, True = Yes
boolean, ask user for input - Did user enter a valid input? if so, append input to users_choice list.
tuple, display_zonk - returns a tuple containg two lists (doors that are zonks and possible doors you can switch to). Returns None if X > len of door_options - 2 (winning door and last users selection) or if user has not made a selection.
boolean set_been_asked - returns the value of what has_been_asked_to_switched is set to.
int get_number_of_options - returns how many doors this game is played with.
int get_door - returns the number of a door. Return None if index in invalid
int get_winning_door  - returns the index of the winning door
int get_users_choice - returns the user's most recent choice. If user has not picked a door, function returns None

Member variables:xlsxwriter
list of int users_choice - list of choices users made.
lint of door values door_options - list of possible door options
int winning_door - index of winning door
boolean has_been_asked_to_switched - keeps track of if the user has been asked to switch doors or not.

"""
import random
import xlsxwriter

class lets_make_a_deal():
    def __init__(self, list_of_possible_doors):
        self.users_choice = []
        self.door_options = list_of_possible_doors
        self.winning_door = random.randint(0, len(self.door_options) - 1)
        self.has_been_asked_to_switched = False

    def display_current_status(self):
        if self.users_choice != [] and self.winning_door == self.users_choice[-1]:
            return True
        return False

    def ask_user_input(self, selection):
        if selection >= 0 and selection < len(self.door_options):
            self.users_choice.append(selection)
            return True
        return False

    def set_been_asked(self):
        self.has_been_asked_to_switched = True
        return True

    def display_zonk(self, display_amount=1):
        if self.users_choice == [] or display_amount > len(self.door_options) - 2:
            return None
        possible_zonks = list(range(0, len(self.door_options)))
        displayed_zonks = []
        del possible_zonks[self.users_choice[-1]]
        if self.winning_door != self.users_choice[-1]:
            if self.users_choice[-1] < self.winning_door:
                del possible_zonks[self.winning_door - 1]
            else:
                del possible_zonks[self.winning_door]
        for _ in range(0, display_amount):
            random_index = random.randint(0, len(possible_zonks) - 1)
            displayed_zonks.append(possible_zonks[random_index])
            del possible_zonks[random_index]
        if self.winning_door != self.users_choice[-1]:
            possible_zonks.append(self.winning_door)
        return displayed_zonks, possible_zonks

    def get_number_of_options(self):
        return len(self.door_options)

    def get_door(self, index):
        if index >= 0 and index < len(self.door_options):
            return self.door_options[index]
        return None

    def get_winning_door(self):
        return self.winning_door

    def get_users_choice(self, ):
        if self.users_choice != []:
            return self.users_choice[-1]
        return None

def playing_the_game():
    doors =  ["A", "B", "C"]
    game = lets_make_a_deal(doors)
    print("Welcome to the Monty Hall problem game!")
    if game.ask_user_input(int(input("Which door number would you like to select? (1-" + str(game.get_number_of_options()) + ")")) - 1):
        zonk_result = game.display_zonk()
        game.set_been_asked()
        print()
        print("The door you selected was : " + str(game.get_door(game.get_users_choice())))
        print("Door " + str(game.get_door(zonk_result[0][0])) + " is a Zonk")
        if input("Would you like to change doors? (Y/N)").lower() == "y":
            game.ask_user_input(zonk_result[1][0])
        print()
        if game.display_current_status():
            print("YOU HAVE WON THE GAME!")
        else:
            print("You lost the game =(")
            print("The door you selected was : " + str(game.get_door(game.get_users_choice())))
        print("The winning door was : " + str(doors[game.get_winning_door()]))
    else:
       print("Game has ended because you do not know how to follow directions.")

def automate_game(num_of_games = 1, user_changes = True):
    workbook = xlsxwriter.Workbook('Monty Hall.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "First Door")
    worksheet.write(0, 1, "Zonk Door")
    worksheet.write(0, 2, "Second Door")
    worksheet.write(0, 3, "Game Result")
    worksheet.write(0, 4, "Winning Door")
    worksheet.write(0,5, "Game ID")
    for row in range (1, num_of_games + 1):
        doors = ["A", "B", "C"]
        game = lets_make_a_deal(doors)
        game.ask_user_input(random.randint(1, len(doors)) - 1)
        worksheet.write(row, 0, str(game.get_door(game.get_users_choice())))
        zonk_result = game.display_zonk()
        worksheet.write(row, 1, str(game.get_door(zonk_result[0][0])))
        if user_changes:
            game.ask_user_input(zonk_result[1][0])
            worksheet.write(row, 2, str(game.get_door(game.get_users_choice())))
        worksheet.write(row, 3, game.display_current_status())
        worksheet.write(row, 4, str(game.get_door(game.get_winning_door())))
        worksheet.write(row, 5, str(row))
    workbook.close()

playing_the_game()

# automate_game(100000, True)

