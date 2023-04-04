from files_manager import main as sorting_manager
from note_book import Note, NoteBook, main as notes_manager
from phone_book import Contact, Email, Birthday, Phone, Address
from phone_bot import main as phone_book_manager
from prettytable import PrettyTable
from weather import main as weather_manager


logo = """ 
______                               _    ___          _     _              _   
| ___ \                             | |  / _ \        (_)   | |            | |  
| |_/ /__ _ __ ___  ___  _ __   __ _| | / /_\ \___ ___ _ ___| |_ __ _ _ __ | |_ 
|  __/ _ \ '__/ __|/ _ \| '_ \ / _` | | |  _  / __/ __| / __| __/ _` | '_ \| __|
| | |  __/ |  \__ \ (_) | | | | (_| | | | | | \__ \__ \ \__ \ || (_| | | | | |_ 
\_|  \___|_|  |___/\___/|_| |_|\__,_|_| \_| |_/___/___/_|___/\__\__,_|_| |_|\__|
________________________________________________________________________________
--------------------------------------------------------------------------------                                                                               
                                                                               
"""
MENU_ITEMS = ["NOTE BOOK", "ADDRESS BOOK", "FOLDER SORTER", "WEATHER"]

COMMANNDS = ['1', '2', '3', '4', 'exit']

chat_in_progress = True


from abc import ABC, abstractmethod


class Commands(ABC):

    @abstractmethod
    def generate_command(self, data):
        pass

class MyCommand(Commands):

    def generate_command(self, command):
        return command

def check_command_validity(func):
    def inner():
        try:
            res = func()
            return res
        except ValueError as err:
            print(err.args[0])
        
    return inner

def create_menu_table():
    menu_table = PrettyTable(["ID", "MAIN MENU"])
    for item in MENU_ITEMS:
        menu_table.add_row([f"{MENU_ITEMS.index(item)+1}", f"{item}"])
    menu_table.min_table_width = 40
    menu_table.max_table_width = 40
    print(menu_table)


def terminate_program():
    global chat_in_progress
    chat_in_progress = False


def greeting():
    print(logo)

@check_command_validity
def start_assistant():
    message = input(
        "\nPlease, type 1,2,3 or 4 in order to choose your tool, or 'exit' to leave >>> ")

    if message not in COMMANNDS:
        message = "This is invalid command.\n"
        raise ValueError(message)
    notes = MyCommand()
    book = MyCommand()
    sort_files = MyCommand()
    # note = notes.generate_command(notes_manager())
    weather = MyCommand()
    # w = weather.generate_command(weather_manager())
    match message:
        case "1":
            notes.generate_command(notes_manager())
            # notes_manager()
        case "2":
            book.generate_command(phone_book_manager())
        case '3':
            sort_files.generate_command(sorting_manager())
        case "4":
            weather.generate_command(weather_manager())
            # weather_manager()
        case "exit":
            terminate_program()


def main():
    command_call = 0

    while chat_in_progress:
        if not command_call:
            greeting()
        create_menu_table()
        start_assistant()
        command_call += 1


if __name__ == "__main__":
        main()

