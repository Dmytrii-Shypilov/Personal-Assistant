from note_book.note_book import Note, NoteBook, main as notes_manager
from prettytable import PrettyTable





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

COMMANNDS = ['exit']

chat_in_progress = True

def create_menu_table():
    menu_table = PrettyTable(["ID","MAIN MENU"])
    for item in MENU_ITEMS:
        menu_table.add_row([f"{MENU_ITEMS.index(item)+1}",f"{item}"])
    menu_table.min_table_width = 40
    menu_table.max_table_width = 40
    print(menu_table)


def terminate_program():
    global chat_in_progress
    chat_in_progress = False


def greeting():
    print(logo)


def start_assistant():
    message = input('Please, type 1,2,3 or 4 in order to choose your tool >>> ')

    match message:
        case "1":
           notes_manager() 
        case "exit":
           terminate_program()


def main():
    command_call = 0

    while chat_in_progress:
        if not command_call:
            greeting()  
        create_menu_table()   
        start_assistant()
        command_call +=1



main()
