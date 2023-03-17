import pickle
import re

from collections import UserDict
from prettytable import PrettyTable


########## COMMANDS ################

COMMANDS = ['add note', 'delete note', 'get by tag', 'get by title', 'exit']



########## CLASSES ##################

class NoteBook(UserDict):
    def add_note(self):
        pass

    def get_note(self):
        pass

    def delete_note(self):
        pass

    def get_notes_by_tag(self):
        pass


class Note:
    def __init__(self, title, content, tag="No tag"):
        self.title = title
        self.tag = tag
        self.content = content



class Tag:
    def __init__(self, value):
        self.value = value

class Title:
    def __init__(self, value):
        self.value = value

class Content:
    def __init__(self, value):
        self.value = value

##############  MODULE FUNCTIONS ################

chat_in_progress = True

def get_instructions(message):
    command_not_found = True

    for command in COMMANDS:
        if message.startswith(command):
            if command == "add note":
                instructions ,text = message.split('#')
                args = instructions.replace(command, '').strip().split(' ')
                return (command, args, text)
            args = message.replace(command, '').strip().split(' ')
            command_not_found = False
            return (command, args)
    if command_not_found:
        raise ValueError(
            f"Assistant: Please enter a valid command: {', '.join(COMMANDS)}")



def add_contact(args):
    pass

def terminate_assitant():
    global chat_in_progress 
    chat_in_progress = False




def main():
    message = input("command: ")
    command_args = get_instructions(message)

    if not command_args:
        return

    command, args = command_args

    print(command)
    print(args)

    match command:
        case "exit":
            terminate_assitant()


while chat_in_progress:
    main()